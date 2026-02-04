extensions = ["sphinx_favicon"]

root_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"
html_static_path = ["gfx"]

favicons = [
    {
        "sizes": "32x32",
        "static-file": "square.svg",
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-32x32.png",
    },
    {
        "sizes": "128x128",
        "static-file": "nested/triangle.svg",
        "href": "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/apple-touch-icon.png",
    },
]
