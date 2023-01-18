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
extensions = ["sphinx_favicon", "sphinx_copybutton"]
source_suffix = [".rst", ".md"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Options for HTML output ---------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
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
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPi",
            "url": "https://pypi.org/project/sphinx-favicon/",
            "icon": "fa-brands fa-python",
        },
    ],
    "logo": {"text": project},
    "use_edit_page_button": True,
    "announcement": "https://raw.githubusercontent.com/12rambau/sphinx-favicon/doc/docs/source/_static/announcment.html",
}

# -- Option for favicons -------------------------------------------------------

favicons = [
    {
        "rel": "apple-touch-icon",
        "size": "180x180",
        "static-file": "apple-touch-icon.png",
    },
    {
        "rel": "icon",
        "type": "image/png",
        "size": "32x32",
        "static-file": "favicon-32x32.png",
    },
    {
        "rel": "icon",
        "type": "image/png",
        "size": "16x16",
        "static-file": "favicon-16x16.png",
    },
    {"rel": "manifest", "static-file": "site.webmanifest"},
    {"rel": "mask-icon", "color": "#2d89ef", "static-file": "safari-pinned-tab.svg"},
    # {
    #    "name": "msapplication-TileColor",
    #    "content": "#2d89ef",
    # },
    # {
    #    "name": "theme-color",
    #    "size": "#ffffff",
    # },
]
