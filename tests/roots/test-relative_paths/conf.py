extensions = ["sphinx-favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"

favicons = [
    {
        "sizes": "32x32",
        "file": "gfx/square.svg",
    },
    {
        "sizes": "64x64",
        "file": "./gfx/circle.svg",
    },
    {
        "sizes": "128x128",
        "file": "../shared/triangle.svg",
    },
]
