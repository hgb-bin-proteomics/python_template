![Ruff](https://github.com/michabirklbauer/python_template/workflows/Ruff%20Linting%20and%20Formatting/badge.svg)
![Pyright](https://github.com/michabirklbauer/python_template/workflows/Type-checking%20with%20Pyright/badge.svg)
![Flake8AndPytest](https://github.com/michabirklbauer/python_template/workflows/Flake8%20and%20pytest/badge.svg)

# Template Repository for Python Scripts

A template repository for linting, testing, GUI building and dockerizing python scripts.

## Checklist

- Replace `YOURUSERNAME` and `IMAGENAME` in `.github/workflows/docker-image.yml` [or delete file].
- Replace test data in `data` with your own data [or delete if you don't have test data].
- Adjust `.gitattributes` according to your needs.
- Adjust `.gitignore` according to your needs.
- Setup your `CITATION.cff` according to your needs [or delete file].
- Replace dummy values in `Dockerfile` and write image instructions.
- Replace copyright name in `LICENSE`.
- Replace lines 10 - 13 and write your script in `main.py`.
- Replace lines 10 - 13 and write your gui in `gui/streamlit_app.py`.
- Replace lines 3 - 6 and write tests in `tests/test_main.py`.
- Add your requirements to `requirements.txt`.
- Document your script using the [numpydoc style](https://numpydoc.readthedocs.io/en/latest/format.html) and [Sphinx](https://www.sphinx-doc.org/):
  - Adjust the configuration to your needs in `docs/conf.py`.
  - Automatically via GitHub Actions:
    - In the repository go to `Settings` ➡️ `Pages` ➡️ `Build and deployment` ➡️ `Source` ➡️ `GitHub Actions`.
    - Select the `gh-pages.yml` / `Deploy Documentation to Pages` workflow.
  - Or build manually:
    - Install Sphinx and the [PyData](https://github.com/pydata/pydata-sphinx-theme) theme: `pip install sphinx pydata-sphinx-theme`.
    - Build documentation with:
      ```
      sphinx-apidoc -f -o docs .
      sphinx-build -b html docs html
      ```
    - Publish documentation [optional]!
    - Serving with GitHub pages needs the addition of an empty `.nojekyll` file to your `/html`.
- Adjust this `README.md` to your needs!

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
