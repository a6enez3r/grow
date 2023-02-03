# grow

Is a tiny python CLI that allows you to search for a phrase in files like `grep` with the optional ability to filter by team or owners specified in a `CODEOWNERS` file. It is invoked with the following syntax:

```sh
grow "class User" "@platform" .github/CODEOWNERS
```

## Quickstart

- Create a virtual environment & install all dependencies

```sh
python3 -m venv venv
source venv/bin/activate
make deps
```

- Install the CLI

```sh
make install
```

- Run `grow --help` to see all available options

```sh
Usage: grow phrase [team] [codeowners]

search for a specific [phrase] in source code paths with the optional ability to filter by
specific [team/owner]

Arguments:
  phrase
  team          (default: *)
  codeowners    (default: ./.github/CODEOWNERS)

Other actions:
  -h, --help   Show the help
```
