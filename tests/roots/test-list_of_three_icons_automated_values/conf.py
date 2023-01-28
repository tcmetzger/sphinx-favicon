extensions = ["sphinx_favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"

favicons = [
    "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-16x16.png",
    {
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-32x32.png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/apple-touch-icon.png",
    },
]
