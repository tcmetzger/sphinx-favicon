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
    "announcement": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/announcment.html",
}

# -- Option for favicons -------------------------------------------------------
favicons = [
    # generic icons compatible with most browsers
    {
        # "rel": "icon",  # automatically set to "icon" if omitted
        # "sizes": "32x32", # automatically set if the file can be read
        # "type": "image/png",  # autogenerated from file type
        "href": "favicon-32x32.png",
    },
    "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    # chrome specific
    "android-chrome-192x192.png",
    # apple icons
    {"rel": "mask-icon", "color": "#2d89ef", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    # msapplications
    {"name": "msapplication-TileColor", "content": "#2d89ef"},
    {"name": "theme-color", "content": "#ffffff"},
    "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/mstile-150x150.png"
    # to show it works as well with absolute urls
]
