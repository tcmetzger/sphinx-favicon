extensions = ["sphinx_favicon"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"
html_static_path = ["gfx"]

favicons = [
    "mstile-150x150.png",
    {"name": "msapplication-TileColor", "content": "#2d89ef"},
    {"name": "theme-color", "content": "#ffffff"},
]
