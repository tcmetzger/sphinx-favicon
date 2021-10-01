from typing import Any, Dict, Optional, Union

import docutils.nodes as nodes
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

SUPPORTED_MIME_TYPES = {
    "bmp": "image/x-ms-bmp",
    "gif": "image/gif",
    "ico": "image/x-icon",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "svg": "image/svg+xml"
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


def create_favicons_meta(
    favicons: Union[Dict[str, str], list[Dict[str, str]]]
) -> Optional[str]:
    """Create ``<link>`` elements for favicons defined in configuration.

    Args:
        favicons (Union[Dict[str, str], list[Dict[str, str]]]): Favicon data
        from configuration. Can be a single dict or a list of dicts.

    Returns:
        str: ``<link>`` elements for all favicons.
    """

    meta_favicons = ""

    # generate meta for favicon dict
    if isinstance(favicons, dict):
        meta_favicons += generate_meta(favicons)
    # generate meta for list of favicon dicts
    elif isinstance(favicons, list) and isinstance(favicons[0], dict):
        for favicon in favicons:
            meta_favicons += generate_meta(favicon) + "\n"
    # generate meta for list of favicon URLs
    elif isinstance(favicons, list):
        for favicon in favicons:
            meta_favicons += generate_meta({"href": favicon}) + "\n"
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

    favicons_meta = None

    if doctree and app.config["favicons"]:
        favicons_meta = create_favicons_meta(app.config["favicons"])
        context["metatags"] += favicons_meta


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("favicons", None, "html")

    app.connect("html-page-context", html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
