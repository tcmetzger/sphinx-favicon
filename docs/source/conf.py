"""Sphinx configuration file for sphinx-favicon documentation."""

# -- imports and read config ---------------------------------------------------
import datetime as dt

import pkg_resources

version = pkg_resources.require("sphinx-favicon")[0].version
year = dt.datetime.now().year

# -- Project information -------------------------------------------------------
project = "Sphinx Favicon"
copyright = f"{year}, Timo Metzger"
author = "Timo Metzger"
release = version

# -- General configuration -----------------------------------------------------
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx_favicon",
    "sphinx_copybutton",
    "sphinx_design",
]
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
    "announcement": (
        "<p>Between v0.2 and v1.0, the module name of the extension changed to better "
        "conform with Python standards. Please update the name used in the extension "
        'list of your <code class="docutils literal notranslate"><span class="pre">'
        'conf.py</span></code> from <code class="docutils literal notranslate">'
        '<span class="pre">sphinx-favicon</span></code> to '
        '<code class="docutils literal notranslate"><span class="pre">'
        "sphinx_favicon</span></code>!</p>"
    ),
}

# -- Option for favicons -------------------------------------------------------
favicons = [
    # generic icons compatible with most browsers
    {"href": "favicon-32x32.png"},
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
