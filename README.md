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

TBD (PyPi, pip)

## Usage

After installing sphinx-favicon, you can configure the extension directly in
`conf.py`.

Currently, this extension requires absolute paths for your favicon files. Make
sure you know the URL of all your favicon files, for example by adding the files
to [Sphinx' `html_static_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path).

First, add `"sphinx-favicon"` to the list of extensions:

```python
extensions = [
    "sphinx-favicon",
]
```

Next, you have several options to define favicons:

### Option A: Provide detailed metadata as a list of dicts

Use a list of dicts for maximum control over the favicons added to your html
document. For example:

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
<link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">
```

To make things easier for you, sphinx-favicon can also add some metadata to each
favicon's `<link>` element automatically:

* If you don't provide any information about the `"rel"` argument,
sphinx-favicon automatically adds `rel="icon"`.
* if you don't provide any information about the `"type"` argument,
sphinx-favicon automatically determines the MIME type based on the image's
file name extension.
* Currently, sphinx-favicon is not able to automatically read a file's size in
pixels as required for the `"size"` argument. If you don't provide information
about a favicon file's pixel size, the `"size"` argument will be omitted for
that favicon image.

Therefore, the following, simplified configuration generates the exact same
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

## Contribute

To contribute to this extension, open an issue or make a pull request to the
repository on GitHub.

Additional dependencies for development are listed in the file
`requirements.txt` in the repository. All Python code should be formatted with
[Black](https://github.com/psf/black).
