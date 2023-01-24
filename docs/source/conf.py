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
    # generic icons compatible with most browsers
    {
        # "rel": "icon",  # automatically set to "icon" if ommitted
        "size": "32x32",
        # "type": "image/png",  # autogenerated from file type
        "href": "favicon-32x32.png",
    },
    {"size": "16x16", "href": "favicon-16x16.png"},
    {"rel": "shortcut icon", "size": "any", "href": "favicon.ico"},
    # chrome specific
    {"size": "192x192", "href": "_static/android-chrome-192x192.png"},
    # apple icons
    {"rel": "mask-icon", "color": "#2d89ef", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "size": "180x180", "href": "apple-touch-icon.png"},
    # msapplications
    {"name": "msapplication-TileColor", "content": "#2d89ef"},
    {"name": "theme-color", "size": "#ffffff"},
    {"href": "mstile-150x150.png"},
]
