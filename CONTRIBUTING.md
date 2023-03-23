## Details

This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution

## Contributions

To make a contribution, create your own fork.

Then run `make develop` to install all the dependencies

Once you write your changes (and corresponding tests), check for any regressions by running `make test`

Before making a PR, check for any linting errors with `make lint`. Many of these can be fixed by running `make format`
