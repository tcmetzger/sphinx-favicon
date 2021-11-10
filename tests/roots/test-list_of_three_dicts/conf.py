extensions = ["sphinx-favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"

favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "href": "https://secure.example.com/favicon/favicon-16x16.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "href": "https://secure.example.com/favicon/favicon-32x32.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
        "type": "image/png",
    },
]
