extensions = ["sphinx-favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"
html_static_path = ["gfx"]

favicons = [
    {
        "sizes": "32x32",
        "static-file": "square.svg",
        "href": "https://secure.example.com/favicon/favicon-32x32.png",
    },
    {
        "sizes": "128x128",
        "static-file": "nested/triangle.svg",
        "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
    },
]
