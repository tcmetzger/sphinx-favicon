extensions = ["sphinx-favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"
html_static_path = ["gfx"]

favicons = [
    {
        "sizes": "32x32",
        "static-file": "square.svg",
    },
    {
        "sizes": "128x128",
        "static-file": "nested/triangle.svg",
    },
]
