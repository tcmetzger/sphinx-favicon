extensions = ["sphinx_favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"

favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-16x16.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-32x32.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/apple-touch-icon.png",
        "type": "image/png",
    },
]
