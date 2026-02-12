extensions = ["sphinx_favicon"]

root_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"
html_static_path = ["gfx"]

favicons = [
    {
        "sizes": "32x32",
        "href": "square.svg",  # use href
    },
    {
        "sizes": "128x128",
        "static-file": "nested/triangle.svg",  # use outdated static-file
    },
    "circle.svg",  # use nothing but filename
]
