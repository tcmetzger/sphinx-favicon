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
      SVG, or PNG files).

    Args:
        favicon (Dict[str, str]): Favicon data

    Returns:
        str: Favicon meta tag
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
    """Return a modified version of the icon attributes replacing ``static-file``
    with the correct ``href``.
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
        pathto (Callable): Sphinx helper_ function to handle relative URLs
        favicons (FaviconsDef): Favicon data from configuration.
            Can be a single dict or a list of dicts.

    Returns:
        str: ``<link>`` elements for all favicons.

    .. _helper: https://www.sphinx-doc.org/en/master/templating.html#patht
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
            """
            Invalid config value for favicon extension. Custom favicons will not
            be included in build.
            """
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

    if doctree and app.config["favicons"]:
        pathto: Callable = context["pathto"]  # should exist in a HTML context
        favicons_meta = create_favicons_meta(pathto, app.config["favicons"])
        context["metatags"] += favicons_meta


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("favicons", None, "html")
    app.connect("html-page-context", html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
