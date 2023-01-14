"""Sphinx extension to add custom favicons.

With sphinx-favicon, you can add custom favicons to your Sphinx html documentation quickly and easily.

You can define favicons directly in your conf.py, with different rel attributes such as "icon" or "apple-touch-icon" and any favicon size.

The sphinx-favicon extension gives you more flexibility than the standard favicon.ico supported by Sphinx. It provides a quick and easy way to add the most important favicon formats for different browsers and devices.
"""

from typing import Any, Callable, Dict, List, Optional, Union
from urllib.parse import urlparse

import docutils.nodes as nodes
from sphinx.application import Sphinx

FaviconsDef = Union[Dict[str, str], List[Dict[str, str]]]

OUTPUT_STATIC_DIR = "_static"
FILE_FIELD = "static-file"
"""field in the ``FaviconsDef`` pointing to file in the ``html_static_path``"""

SUPPORTED_MIME_TYPES = {
    "bmp": "image/x-ms-bmp",
    "gif": "image/gif",
    "ico": "image/x-icon",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "svg": "image/svg+xml",
}


def generate_meta(favicon: Dict[str, str]) -> str:
    """Generate metatag based on favicon data.

    Default behavior:
    - If favicon data contains no ``rel`` attribute, sets ``rel="icon"``
    - If no ``size`` attribute is provided, ``size`` will be omitted
    - If no favicon MIME type is provided, the value for ``type`` will be
      based on the favicon's file name extension (for BMP, GIF, ICO, JPG, JPEG,
      SVG, or PNG files)

    Args:
        favicon: Favicon data

    Returns:
        Favicon meta tag
    """
    rel = favicon.get("rel", "icon")
    href = favicon["href"]
    meta = f'    <link rel="{rel}" href="{href}"'

    # Read "sizes" from config. Omit sizes if not provided.
    sizes = favicon.get("sizes", None)
    if sizes:
        meta += f' sizes="{sizes}"'

    # Set MIME type. Detect MIME type if not provided. Omit "type=" if not detectable
    favicon_type = favicon.get("type", None)
    favicon_file_ending = href.split(".")[-1]
    if favicon_type:
        meta += f' type="{favicon_type}"'
    elif favicon_file_ending in SUPPORTED_MIME_TYPES.keys():
        favicon_type = SUPPORTED_MIME_TYPES[favicon_file_ending]
        meta += f' type="{favicon_type}"'

    meta += ">"

    return meta


def _static_to_href(pathto: Callable, favicon: Dict[str, str]) -> Dict[str, str]:
    """Replace static ref to fully qualified href.

    if the ``href`` is a relative path then it's replaced with the correct ``href``. We keep checking for ``static-file`` for legacy reasons.
    If both ``static-file`` and ``href`` are provided, ``href`` will be ignored.

    Args:
        pathto: Sphinx helper_ function to handle relative URLs
        favicon: The favicon description as set in the conf.py file

    Returns:
        The favicon with a fully qualified href
    """
    # legacy check for "static-file"
    if FILE_FIELD in favicon:
        favicon["href"] = favicon.pop(FILE_FIELD)

    # check if link is absolute
    link = favicon["href"]
    is_absolute = bool(urlparse(link).netloc) or link.startswith("/")

    # if the link is absolute do nothing, else replace it with a full one
    if not is_absolute:
        path = f"{OUTPUT_STATIC_DIR}/{link}"
        favicon["href"] = pathto(path, resource=True)

    return favicon


def create_favicons_meta(pathto: Callable, favicons: FaviconsDef) -> Optional[str]:
    """Create ``<link>`` elements for favicons defined in configuration.

    Args:
        pathto: Sphinx helper_ function to handle relative URLs
        favicons: Favicon data from configuration. Can be a single dict or a list of dicts.

    Returns:
        ``<link>`` elements for all favicons.

    See Also:
        https://www.sphinx-doc.org/en/master/templating.html#path
    """
    # force cast the favicon config as a list
    if isinstance(favicons, dict):
        favicons = [favicons]

    # read this list and create the links for each item
    meta_favicons = []
    for favicon in favicons:
        if isinstance(favicon, str):
            favicon = {"href": favicon}
        tag = generate_meta(_static_to_href(pathto, favicon))
        meta_favicons.append(tag)

    return "\n".join(meta_favicons)


def html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: nodes.document,
) -> None:
    """Update the html page context by adding the favicons.

    Args:
        app: The sphinx application
        pagename: the name of the page as string
        templatename: the name of the template as string
        context: the html context dictionnary
        doctree: the docutils document tree
    """
    if doctree and app.config["favicons"]:
        pathto: Callable = context["pathto"]  # should exist in a HTML context
        favicons_meta = create_favicons_meta(pathto, app.config["favicons"])
        context["metatags"] += favicons_meta


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add custom configuration to shinx app.

    Args:
        app: the Sphinx application

    Returns:
        the 2 parralel parameters set to ``True``
    """
    app.add_config_value("favicons", None, "html")
    app.connect("html-page-context", html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
