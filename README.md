# sphinx-favicon

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Black badge](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/sphinx-favicon?logo=python&logoColor=white)](https://pypi.org/project/sphinx-favicon/)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/tcmetzger/sphinx-favicon/basic-ci.yml?logo=github&logoColor=white)

**A Sphinx extension to add custom favicons**

With sphinx-favicon, you can add custom favicons to your Sphinx html
documentation quickly and easily.

You can define favicons directly in your `conf.py`, with different `rel`
attributes such as [`"icon"`](https://html.spec.whatwg.org/multipage/links.html#rel-icon)
or [`"apple-touch-icon"`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html) and
any favicon size.

The sphinx-favicon extension gives you more flexibility than the [standard
`favicon.ico` supported by Sphinx](https://www.sphinx-doc.org/en/master/templating.html?highlight=favicon#favicon_url). It provides a quick and easy way to add the most
important favicon formats for different browsers and devices.

## Installation

Use ``pip`` to install sphinx-favicon in your environment:

```sh
pip install sphinx-favicon
```

## Usage

After installing sphinx-favicon, you can configure the extension directly in
`conf.py` (see [Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html)
in the Sphinx documentation for more information about this file).

There are two ways to include favicon files in your configuration:

* Either use an **absolute URL** for a favicon file (beginning with `http://` or
  `https://`). If you use an absolute URL, use the `"href"` parameter. See below
  for examples.
* Or use a **local static file** as a favicon. Make sure you place your local
  static favicon file(s) inside a directory listed in [Sphinx' `html_static_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path). If you use a relative path, use the `"static-file"` parameter. See below for
  examples.

To configure sphinx-favicon, first add `"sphinx-favicon"` to the list of
extensions:

```python
extensions = [
    "sphinx-favicon",
]
```

Next, you have several options to define favicons:

### Option A: Provide detailed metadata as a list of dicts

Use a list of dicts for maximum control over the favicons added to your html
document. You can use the following parameters to define a favicon:

* ``rel``: a value for the favicon's ``rel`` attribute, usually either the
standard [`"icon"`](https://html.spec.whatwg.org/multipage/links.html#rel-icon)
or a custom extension like [`"apple-touch-icon"`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html)
* ``sizes``: a value for the [favicon's ``sizes`` attribute](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-sizes)
* ``href``: the **absolute URL** to the favicon's image file (not required if you use the ``static-file`` parameter, see below)
* ``type``: a value specifying the [favicon's MIME type](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type)
* ``static-file``: the **local static file** corresponding to your icon's image.
   Please notice this path should be relative to a directory listed in
   [Sphinx' `html_static_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path) (usually `_static`). If you define both
   ``static-file`` and ``href``, the value for ``href`` will be ignored.

For example:

```python
html_static_path = ["_static"]  # html_static_path is required if you use the "static-file" parameter

favicons = [
    {
        "rel": "icon",
        "static-file": "icon.svg",  # => use `_static/icon.svg`
        "type": "image/svg+xml",
    },
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
```

Based on this configuration, Sphinx will include the following favicon
information in the HTML `<head>` element:

```html
<link rel="icon" href="_static/icon.svg" type="image/svg+xml">
<link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">
```

Note that the relative path to the favicon's image file in the static directory
will be adjusted according to each html file's location.

To make things easier for you, sphinx-favicon can also add *some* metadata to
each favicon's `<link>` element automatically:

* If you don't provide the `"rel"` argument, sphinx-favicon automatically adds
`rel="icon"`.
* if you don't provide the `"type"` argument, sphinx-favicon automatically
determines the MIME type based on the image's filename extension.
* Currently, sphinx-favicon is not able to automatically read a file's size in
pixels as required for the `"size"` argument. If you don't provide information
about a favicon file's pixel size, the `"size"` argument will be omitted for
that favicon image.

Therefore, the following simplified configuration generates the exact same
HTML result as above:

```python
html_static_path = ["_static"]

favicons = [
    {"static-file": "icon.svg"},  # => use `_static/icon.svg`
    {
        "sizes": "16x16",
        "href": "https://secure.example.com/favicon/favicon-16x16.png",
    },
    {
        "sizes": "32x32",
        "href": "https://secure.example.com/favicon/favicon-32x32.png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
    },
]
```

### Option B: Provide a single dict for just one favicon

If you want to add just one custom favicon, you can also use a simple dict in
`conf.py`:

```python
favicons = {
    "rel": "apple-touch-icon",
    "sizes": "180x180",
    "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
    }
```

Based on this configuration, Sphinx will include the following favicon
information in the `<head>` of every HTML file:

```html
<link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">
```

### Option C: Provide a list of local favicon files or URLs

The quickest way to add favicons is just adding a list of favicon URLs to
`conf.py`.

```python
html_static_path = ["_static"]
favicons = [
    "icon.svg",  # => `_static_/icon.svg`
    "https://secure.example.com/favicon/favicon-16x16.gif",
    "https://secure.example.com/favicon/favicon-32x32.png",
    "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
]
```

Based on this configuration, Sphinx will include the following favicon
information in the HTML `<head>` element:

```html
<link rel="icon" href="_static/icon.svg" type="image/svg+xml">
<link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.gif" type="image/gif">
<link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" type="image/png">
<link rel="icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" type="image/png">
```

Please note that if your URLs don't start with `https://`, `http://` or `/`,
they will be considered a static file inside a directory listed in
[Sphinx' `html_static_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path).

## Contribute

To contribute to this extension, please open an issue or make a pull request to
the repository on GitHub.

Additional dependencies for development are listed in the file
`dev-requirements.txt` in the repository. Use ``pytest -vv`` to run tests.

Please install `pre-commit` Python package and run the following command before commiting your modifications:

```
pre-commit install
```