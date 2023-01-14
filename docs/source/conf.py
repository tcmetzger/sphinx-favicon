"""Sphinx configuration file for sphinx-favicon documentation."""

# -- imports and read config ---------------------------------------------------
import datetime as dt

import pkg_resources

version = pkg_resources.require("sphinx-favicon")[0].version
year = dt.datetime.now().year

# -- Project information -------------------------------------------------------
project = "sphinx-favicon"
copyright = f"{year}, Timo Metzger"
author = "Timo Metzger"
release = version

# -- General configuration -----------------------------------------------------
extensions = ["myst_parser", "sphinx_favicon"]
source_suffix = [".rst", ".md"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Options for HTML output ---------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_context = {
    "display_github": True,
    "github_user": "tcmetzger",
    "github_repo": "sphinx-favicon",
    "github_version": "main/docs/source/",
}

# -- Options for the html theme ------------------------------------------------
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/tcmetzger/sphinx-favicon",
            "icon": "fa-brand fa-github",
        },
        {
            "name": "PyPi",
            "url": "https://pypi.org/project/sphinx-favicon/",
            "icon": "fa-brand fa-python",
        },
    ],
    "logo": {"text": "project"},
    "use_edit_page_button": True,
    # "announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
}
