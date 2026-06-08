![Ruff](https://github.com/michabirklbauer/python_template/workflows/Ruff%20Linting%20and%20Formatting/badge.svg)
![Ty](https://github.com/michabirklbauer/python_template/workflows/Type-checking%20with%20ty/badge.svg)
![Pyright](https://github.com/michabirklbauer/python_template/workflows/Type-checking%20with%20Pyright/badge.svg)
![Flake8AndPytest](https://github.com/michabirklbauer/python_template/workflows/Flake8%20and%20pytest/badge.svg)

# Template Repository for Python Scripts

A template repository for modern python development with [uv](https://docs.astral.sh/uv/)
using [Pydantic](https://pydantic.dev/docs/validation/latest/get-started/),
[Polars](https://pola.rs/), and [Streamlit](https://streamlit.io/).
Linted with [ruff](https://astral.sh/ruff),
type checked with [ty](https://docs.astral.sh/ty/) and [pyright](https://github.com/microsoft/pyright),
and tested with [pytest](https://docs.pytest.org/en/stable/) using
[GitHub Actions](https://docs.github.com/en/actions).

## Checklist

- [ ] Replace `YOURUSERNAME` and `IMAGENAME` in `.github/workflows/docker-image.yml` [or delete file].
- [ ] Replace test data in `data` with your own data [or delete if you don't have test data].
- [ ] Adjust `.gitattributes` according to your needs [or delete file].
- [ ] Adjust `.gitignore` according to your needs.
- [ ] Setup your `CITATION.cff` according to your needs [or delete file].
- [ ] Update attribution in `Dockerfile` and write image instructions.
- [ ] Replace copyright name in `LICENSE`.
- [ ] Update attribution and write your script in `main.py`.
- [ ] Update attribution and write your gui in `app.py`.
- [ ] Update attribution and write tests in `tests/test_main.py`.
- [ ] Add your requirements via `uv add` and to `requirements.txt`.
- [ ] Document your code using the [numpydoc style](https://numpydoc.readthedocs.io/en/latest/format.html) and [Sphinx](https://www.sphinx-doc.org/):
  - Adjust the configuration to your needs in `docs/conf.py`.
  - Automatically via GitHub Actions:
    - In the repository go to `Settings` ➡️ `Pages` ➡️ `Build and deployment` ➡️ `Source` ➡️ `GitHub Actions`.
    - Select the `gh-pages.yml` / `Deploy Documentation to Pages` workflow.
  - Or build manually:
    - Install Sphinx, the [PyData](https://github.com/pydata/pydata-sphinx-theme) theme, and extensions:
      ```bash
      pip install sphinx pydata-sphinx-theme myst-parser sphinx-copybutton
      ```
    - Build documentation with:
      ```bash
      sphinx-apidoc -f -o docs .
      sphinx-build -b html docs html
      ```
    - Publish documentation [optional]!
    - Serving with GitHub pages needs the addition of an empty `.nojekyll` file to your `/html`.
- [ ] Decide on a type checker and delete the other!
- [ ] Adjust this `README.md` to your needs!

## Helpful Commands

- [uv](https://docs.astral.sh/uv/):
  - Add a dependency/package [`pkg`]:
    ```bash
    uv add pkg
    ```
  - Upgrade dependencies/packages:
    ```bash
    uv lock --upgrade
    ```
  - Update environment:
    ```bash
    uv sync
    ```
- [ruff](https://docs.astral.sh/ruff/):
  - Check and fix (fixable) errors:
    ```bash
    ruff check --fix
    ```
  - Check (with explicit config file):
    ```bash
    ruff check --config ruff.toml
    ```
  - Format code:
    ```bash
    ruff format
    ```
  - Format (with explicit config file):
    ```bash
    ruff format --config ruff.toml
    ```
- [ty](https://docs.astral.sh/ty/):
  ```bash
  ty check --config-file ty.toml
  ```
- [pyright](https://microsoft.github.io/pyright/#/):
  ```bash
  pyright
  ```
- [pytest](https://docs.pytest.org/en/stable/):
  ```bash
  pytest -c pytest.ini --durations=10 --durations-min=1.0 tests/
  ```
- [streamlit](https://docs.streamlit.io/):
  ```bash
  uv run streamlit run app.py
  ```

## Getting Help

- Help for this template:
  - [uv](https://docs.astral.sh/uv/): Python project and dependency management.
  - [ruff](https://astral.sh/ruff): Python linter and formatter.
  - [ty](https://docs.astral.sh/ty/): Python type checker.
  - [pyright](https://github.com/microsoft/pyright): Python type checker.
  - [pytest](https://docs.pytest.org/en/stable/): Python testing suit.
  - [GitHub Actions](https://docs.github.com/en/actions): Used for running the above automatically.
- Contact: [micha.birklbauer@gmail.com](mailto:micha.birklbauer@gmail.com)

> [!IMPORTANT]
> The below sections should be adjusted and updated by you!

## Known Issues

[List of known issues](https://github.com/michabirklbauer/python_template/issues)

## Citing

If you are using PLACEHOLDER please cite:
```
Very important title
Important Author, and Another Important Author
Journal of Cool Stuff 2023 12 (3), 4567-4589
DOI: 12.3456/cool-stuff
```

## License

- [MIT](https://github.com/michabirklbauer/python_template/blob/master/LICENSE)

## Contact

- [your.mail@mail.com](mailto:your.mail@mail.com)
