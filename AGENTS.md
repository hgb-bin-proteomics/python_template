# Template Repository for Python Scripts

A template repository for modern python development with [uv](https://docs.astral.sh/uv/)
using [Pydantic](https://pydantic.dev/docs/validation/latest/get-started/),
[Polars](https://pola.rs/), and [Streamlit](https://streamlit.io/).
Linted with [ruff](https://astral.sh/ruff),
type checked with [ty](https://docs.astral.sh/ty/) and [pyright](https://microsoft.github.io/pyright),
and tested with [pytest](https://docs.pytest.org/en/stable/) using
[GitHub Actions](https://docs.github.com/en/actions).

## Repository Structure

- `main.py` is the main entry point and contains all application logic.
- `main.py` should be self contained, do not split application logic into multiple files.
- `main.py` can be renamed to have a more descriptive name.
- `app.py` contains the [Streamlit](https://streamlit.io/) web app code.
- `app.py` should import any necessary functionality from `main.py`.
- Tests should go into the `tests/` directory.
- Every test file should have a `test_` prefix.
- Configuration for [Sphinx](https://www.sphinx-doc.org/) should go into the `docs/` directory.

## Setup

- Make sure to install [uv](https://docs.astral.sh/uv/getting-started/installation/).
- If python is already installed, uv can easily be installed via `pip install uv`.
- Or prompt the user to install it preemptively.
- Execute all commands in a shell (e.g. bash) in the repository root.

## Managing the python Environment

- Use [uv](https://docs.astral.sh/uv/) to manage the projects python environment.
- When using uv for the first time in this repository, make sure to call `uv sync --all-groups` to install all tools and dependency groups.
- Use `uv add <pkg>` to add and install a package.
- Use `uv add --dev <pkg>` to add and install a package needed only for development.
- Use `uv add --group docs <pkg>` to add and install a package needed only for documentation.

## Code Quality and Style

- Use [ruff](https://docs.astral.sh/ruff/) for linting.
- Run `uv run ruff check --config ruff.toml` to make sure all the python code in the repository passes linting.
- Make sure to use an up-to-date version of ruff, e.g. by running `uv lock --upgrade-package ruff`.
- Linting errors might be fixable with `uv run ruff check --config ruff.toml --fix`.
- Use [ruff](https://docs.astral.sh/ruff/) for code formatting.
- Run `uv run ruff format --config ruff.toml` to format all python files.
- Make sure to use an up-to-date version of ruff, e.g. by running `uv lock --upgrade-package ruff`.
- Check with `uv run ruff format --config ruff.toml --check` that all python files in the repository are properly formatted.
- Use type annotation wherever possible.
- Avoid the `Any` type unless it makes sense.
- Make sure to follow [PEP 585](https://peps.python.org/pep-0585/) standard for type annotation.
- Use `typing.Optional` for optional arguments instead of `X | None`.
- Prompt the user to select either [ty](https://docs.astral.sh/ty/) or [pyright](https://microsoft.github.io/pyright) for type checking.
- Run `uv run ty check --config-file ty.toml` to type check all python files with ty.
- Run `uv run pyright --warnings` to type check all python files with pyright.
- Make sure to use an up-to-date version of ty, e.g. by running `uv lock --upgrade-package ty`.
- Make sure to use an up-to-date version of pyright, e.g. by running `uv lock --upgrade-package pyright`.
- Make sure to follow python naming conventions and code style, e.g. defined via [PEP 8](https://peps.python.org/pep-0008/).
- Use [Pydantic](https://pydantic.dev/docs/validation/latest/get-started/) for classes as also demonstrated in the `main.py` file.
- Function parameters should ideally be type checked using `isinstance()` or other suitable python type checking methods, do not use the [Typeguard](https://github.com/agronholm/typeguard) library for this purpose unless specifically prompted.
- Use `logging` for logging state and events of python code.
- Use `argparse` in the `main.py` file to parse commandline arguments.

## Testing

- Use [pytest](https://docs.pytest.org/en/stable/) for testing python code.
- Configuration for pytest should go into the `pytest.ini` file.
- Tests should go into the `tests/` directory.
- Every test file should have a `test_` prefix.
- Run `uv run pytest -c pytest.ini --durations=10 --durations-min=1.0 tests/` to run all tests. The process should exit with code 0 if all tests pass.

## Documentation

- Use [numpydoc style](https://numpydoc.readthedocs.io/en/latest/format.html) for inline documentation.
- Use [Sphinx](https://www.sphinx-doc.org/) for setting up `html` documentation.
- Configuration for Sphinx should go into the `docs/` directory.
- The `html` documentation can be built locally by running `uv run sphinx-apidoc -f -o docs .` and `uv run sphinx-build -b html docs html`.

## Docker

- The Docker image can be built with `docker build . -t Dockerfile -t <name>` where `<name>` is the repository name.
- Make sure to have a clean image build context, e.g. by running `git clean -f -d -X`.

## CI/CD

- Workflows for [GitHub Actions](https://docs.github.com/en/actions) can be found in `.github/workflows`.
- Pull requests that target `master` should come from the `develop` branch when using this template.
- The `branch-protection.yml` workflow can be removed if pull requests targeting `master` should be allowed from any branch.
- The `gh-pages.yml` workflow automatically deploys the `html` documentation to [GitHub Pages](https://docs.github.com/en/pages).
