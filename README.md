# sphinx-favicon

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
`conf.py`.

If you are using **absolute paths** for your favicon files,
make sure you know their URL, for example by adding the
files to [Sphinx' `html_static_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path).

First, add `"sphinx-favicon"` to the list of extensions:

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
* ``href``: the **absolute path** to the favicon's image file
* ``type``: a value specifying the [favicon's MIME type](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type)
* ``file``: if you want to use a file in the same directory as your documents,
  you can specify a relative path instead of the ``href`` attibute.
  Please notice this path is solved according to your ``conf.py`` file.

For example:

```python
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
        "rel": "icon",
        "file": "./assets/icon.svg",
        "type": "image/svg+xml",
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
information in the `<head>` of every HTML file:

```html
<link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="_images/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">
```

To make things easier for you, sphinx-favicon can also add some metadata to each
favicon's `<link>` element automatically:

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
favicons = [
    {
        "sizes": "16x16",
        "href": "https://secure.example.com/favicon/favicon-16x16.png",
    },
    {
        "sizes": "32x32",
        "href": "https://secure.example.com/favicon/favicon-32x32.png",
    },
    {"file": "./assets/icon.svg"},
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

### Option C: Provide a list of favicon URLs

The quickest way to add favicons is just adding a list of favicon URLs to
`conf.py`.

```python
favicons = [
    "https://secure.example.com/favicon/favicon-16x16.gif",
    "https://secure.example.com/favicon/favicon-32x32.png",
    "asserts/icon.svg",
    "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
]
```

Based on this configuration, Sphinx will include the following favicon
information in the `<head>` of every HTML file:

```html
<link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.gif" type="image/gif">
<link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" type="image/png">
<link rel="icon" href="_images/icon.svg" type="image/svg+xml">
<link rel="icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" type="image/png">
```

Please notice that if your URLs don't start with `https://`, `http://` or `/`,
they will be considered relative to the `conf.py` file.

## Contribute

To contribute to this extension, please open an issue or make a pull request to
the repository on GitHub.

Additional dependencies for development are listed in the file
`requirements.txt` in the repository. All Python code should be formatted with
[Black](https://github.com/psf/black).
