# Sphinx Favicon

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Black badge](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/sphinx-favicon?logo=python&logoColor=white)](https://pypi.org/project/sphinx-favicon/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-favicon?color=orange&logo=python&logoColor=white)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/tcmetzger/sphinx-favicon/basic-ci.yml?logo=github&logoColor=white)
![Read the Docs (version)](https://img.shields.io/readthedocs/sphinx-favicon/latest?logo=readthedocs&logoColor=white)

> **Note: Updating from Version 0.2 to Version 1.0**
>
> Between v0.2 and v1.0, the module name of the extension changed to better conform with Python standards. Please update the name used in the extension list of your `conf.py` from `sphinx-favicon` to `sphinx_favicon`!

**A Sphinx extension to add custom favicons**

With Sphinx Favicon, you can add custom favicons to your Sphinx html
documentation quickly and easily.

You can define favicons directly in your `conf.py`, with different `rel`
attributes such as [`"icon"`](https://html.spec.whatwg.org/multipage/links.html#rel-icon)
or [`"apple-touch-icon"`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html) and
any favicon size.

The Sphinx Favicon extension gives you more flexibility than the [standard
`favicon.ico` supported by Sphinx](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon). It provides a quick and easy way to add the most
important favicon formats for different browsers and devices.

## Installation

Use ``pip`` to install Sphinx Favicon in your environment:

```sh
pip install sphinx-favicon
```

## Usage

After installing **sphinx-favicon**, add it to your `conf.py` extension list:

```python
extensions = ["sphinx_favicon"]
```

Then configure the favicon links using the `favicons` parameter (`html_static_path` is mandatory if you use relative path):

```python
html_static_path = ["_static"]

favicons = [
    {"href": "icon.svg"},  # => use `_static/icon.svg`
    {"href": "https://secure.example.com/favicon/favicon-16x16.png"},
    {"href": "https://secure.example.com/favicon/favicon-32x32.png"},
    {
        "rel": "apple-touch-icon",
        "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
    },
]
```

Based on this configuration, Sphinx will include the following favicon information in the HTML `<head>` element:

```html
<link rel="icon" href="_static/icon.svg" type="image/svg+xml">
<link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">
```

For more details and more advanced usage, please see the
[documentation](https://sphinx-favicon.readthedocs.io).

## Contribution

Contributions of any kind are welcome. Please see the
[contribution](https://sphinx-favicon.readthedocs.io/en/latest/contribute.html) section of
our documentation for more information.
