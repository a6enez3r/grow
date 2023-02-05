"""
    grow: git grep with ability to filter paths by owner team in codeowners
"""
from clize import run

from grow import Grow


if __name__ == "__main__":
    run({"search": Grow.search, "version": Grow.version})
