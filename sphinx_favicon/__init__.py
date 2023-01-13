"""Sphinx extension to add custom favicons.

With sphinx-favicon, you can add custom favicons to your Sphinx html documentation quickly and easily.

You can define favicons directly in your conf.py, with different rel attributes such as "icon" or "apple-touch-icon" and any favicon size.

The sphinx-favicon extension gives you more flexibility than the standard favicon.ico supported by Sphinx. It provides a quick and easy way to add the most important favicon formats for different browsers and devices.
"""

from typing import Any, Callable, Dict, List, Optional, Union

import docutils.nodes as nodes
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

FaviconsDef = Union[Dict[str, str], List[Dict[str, str]]]

OUTPUT_STATIC_DIR = "_static"
FILE_FIELD = "static-file"
"""field in the ``FaviconsDef`` pointing to file in the ``html_static_path``"""
ABSOLUTE_HREF_STARTERS = ("https://", "http://", "/")
# `/` points to a file relative to HTML's <base />, so it should be treated as
# absolute

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
        Favicon link or meta tag
    """
    # get the tag of the output
    tag = "link"

    # prepare all the tag parameters and leave them in the favicon dict

    # to raise an error if not set
    favicon["href"]

    # default to "icon"
    favicon.setdefault("rel", "icon")

    # set the type. if type is not set try to guess it from the file extention
    type_ = favicon.get("type")
    if not type_:
        extention = favicon["href"].split(".")[-1]
        if extention in SUPPORTED_MIME_TYPES.keys():
            type_ = SUPPORTED_MIME_TYPES[extention]
    if type_ is not None:
        favicon["type"] = type_

    # build the html element
    parameters = [f"{k}={v}" for k, v in favicon.items()]
    html_element = f"    <{tag} {' '.join(parameters)}>"
    print(html_element)
    return html_element


def _static_to_href(pathto: Callable, favicon: Dict[str, str]) -> Dict[str, str]:
    """Replace static ref to fully qualified href.

    If a ``static-file`` is provided, returns a modified version of the icon attributes replacing ``static-file`` with the correct ``href``.
    If both ``static-file`` and ``href`` are provided, ``href`` will be ignored.

    Args:
        pathto: Sphinx helper_ function to handle relative URLs
        favicon: The favicon description as set in the conf.py file

    Returns:
        The favicon with a fully qualified href
    """
    if FILE_FIELD in favicon:
        attrs = favicon.copy()
        attrs["href"] = pathto(
            f"{OUTPUT_STATIC_DIR}/{attrs.pop(FILE_FIELD)}", resource=True
        )
        return attrs
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
    meta_favicons = ""

    # generate meta for favicon dict
    if isinstance(favicons, dict):
        meta_favicons += generate_meta(_static_to_href(pathto, favicons))
    # generate meta for list of favicon dicts
    elif isinstance(favicons, list) and isinstance(favicons[0], dict):
        for favicon in favicons:
            meta_favicons += generate_meta(_static_to_href(pathto, favicon)) + "\n"
    # generate meta for list of favicon URLs
    elif isinstance(favicons, list):
        for favicon in favicons:
            if any(favicon.startswith(x) for x in ABSOLUTE_HREF_STARTERS):
                attrs = {"href": favicon}
            else:
                attrs = _static_to_href(pathto, {FILE_FIELD: favicon})
            meta_favicons += generate_meta(attrs) + "\n"
    else:
        logger.warning(
            "Invalid config value for favicon extension."
            "Custom favicons will notbe included in build."
        )
        return None

    return meta_favicons


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
