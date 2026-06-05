# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Example"
copyright = "2026, Your Name"
author = "Your Name"
version = "0.1"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["build"]
root_doc = "index"
autosummary_generate = True
autodoc_default_options = {"members": True, "inherited-members": False}
python_maximum_signature_line_length = 88

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Example"
html_short_title = "Example"
html_logo = "icons/icon.png"
html_favicon = "icons/favicon.png"
html_theme = "pydata_sphinx_theme"
html_show_sourcelink = False
html_theme_options = {
    "logo": {
        "alt_text": "Example logo",
        "text": "Example logo",
        "image_light": "icons/icon.png",
        "image_dark": "icons/icon.png",
    },
    "header_links_before_dropdown": 5,
    "external_links": [
        {"name": "uv", "url": "https://docs.astral.sh/uv/"},
        {"name": "ruff", "url": "https://astral.sh/ruff"},
        {"name": "ty", "url": "https://docs.astral.sh/ty/"},
        {"name": "pyright", "url": "https://github.com/microsoft/pyright"},
        {"name": "pytest", "url": "https://docs.pytest.org/en/stable/"},
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/michabirklbauer/python_template",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
    "show_toc_level": 2,
    "use_edit_page_button": False,
    "primary_sidebar_end": ["indices.html"],
}
html_context = {
    "github_url": "https://github.com",
    "github_user": "michabirklbauer",
    "github_repo": "python_template",
    "github_version": "master",
    "doc_path": "docs",
    "default_mode": "auto",
}
