"""
grow:   git grep with ability to filter paths by owner team
        used to check whether a string exists in a given team's files

        for instance: to check whether the phrase 'database = "__all__"'
        exists in any of the files owned by '@klaviyo/mobile-delivery'
        update phrase and team variables and run :-

            python3 grow 'database = "__all__"' '@klaviyo/mobile-delivery'

        NOTE :- needs deps installed with the following command:

                    python3 -m pip install codeowners tabulate clize

             :- you can override team, codeowners, and phrase
                using environment variables (should note subprocess
                might be finnicky with quotes especially for phrase)
"""
import os
import subprocess
from pathlib import Path

from codeowners import CodeOwners
from tabulate import tabulate

from grow import _version

__version__ = _version.get_versions()["version"]


class Grow:
    """git grep with ability to filter paths by owner team"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def version():
        """get current version"""
        return __version__

    @staticmethod
    def search(
        phrase,
        team: str = "*",
        codeowners: str = os.environ.get(
            "GROW_CODEOWNERS_PATH",
            "./.github/CODEOWNERS",
        ),
    ):
        """
        search for a specific [phrase] in source code paths with the optional ability to filter
        by specific [team/owner]
        """
        repo_path = codeowners.split(".github")[0]
        files = (
            subprocess.check_output(
                ["git", "grep", "--full-name", "--name-only", phrase],
                cwd=repo_path,
            )
            .decode("utf-8")
            .strip()
            .split("\n")
        )
        codeowners_data = Path(codeowners).read_text(encoding="utf-8")
        owners = CodeOwners(codeowners_data)
        print(
            f"\nSearch Stats: {Grow.OKBLUE}{phrase}{Grow.ENDC} \n\n",
            f"Unique Owners:     {Grow.OKCYAN}{len({path[2][0][1] for path in owners.paths})}{Grow.ENDC}\n",  # pylint: disable=line-too-long
            f"Total Paths:       {Grow.OKCYAN}{len(owners.paths)}{Grow.ENDC}\n",
            f"Matching Paths:    {Grow.OKCYAN}{len(files)}{Grow.ENDC}\n",
            f"Repo Path:         {Grow.OKCYAN}{repo_path}{Grow.ENDC}\n",
        )

        if team != "*":
            table = [
                [file_path, owners.of(file_path)[0][1]]
                for file_path in files
                if owners.of(file_path)[0][1] == team
            ]
        else:
            table = [[file_path, owners.of(file_path)[0][1]] for file_path in files]

        if len(table) != 0:
            print(tabulate(table, headers=["File Path", "Owner"]))
            print()

        color = Grow.FAIL if len(table) == 0 else Grow.OKGREEN
        print(
            f"{Grow.BOLD}Found: {color}{len(table)}{Grow.ENDC} {Grow.BOLD}files that{Grow.ENDC}"
            f"{Grow.BOLD}contain the phrase: {color}{phrase}{Grow.ENDC}\n",
            sep=" ",
        )
