from typing import Any, Dict, Optional, Union

import docutils.nodes as nodes
from sphinx.application import Sphinx
# from sphinx.util import logger
from sphinx.util import logging

logger = logging.getLogger(__name__)

SUPPORTED_MIME_TYPES = {
    "png": "image/png",
    "ico": "image/x-icon",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "gif": "image/gif",
    "bmp": "image/x-ms-bmp",
}

def _generate_meta(favicon: Dict[str, str]) -> Optional[str]:
    # ToDo: if not mime_type: _detect_mime_type(href) - if still None: leave out mime type

    rel = favicon.get("rel", "icon") # default to rel=icon if no rel provided
    href =  favicon["href"]
    meta = f'<link rel="{rel}" href="{href}"'

    # Read "sizes" from config. Omit sizes if not provided.
    sizes = favicon.get("sizes", None)
    if sizes:
        meta += f' sizes="{sizes}"'

    # Set MIME type. Detect MIME type if not provided. Omit "type=" if not detectable
    favicon_type = favicon.get("type", None)
    if favicon_type:
        meta += f' type="{favicon_type}"'
    elif href.split(".")[-1] in SUPPORTED_MIME_TYPES.keys():
        favicon_type = SUPPORTED_MIME_TYPES[href.split(".")[-1]]
        meta += f' type="{favicon_type}"'

    meta += ">"

    return meta

def create_favicons_meta(favicons: Union[Dict[str, str], list[Dict[str, str]]]) -> Optional[str]:
    meta_favicons = ""

    # generate meta for favicon dict
    if isinstance(favicons, dict):
        meta_favicons += _generate_meta(favicons)
    # generate meta for list of favicon dicts
    elif isinstance(favicons, list) and isinstance(favicons[0], dict):
        for favicon in favicons:
            meta_favicons += _generate_meta(favicon) + "\n"
    # generate meta for list of favicon URLs
    elif isinstance(favicons, list):
        for favicon in favicons:
            meta_favicons += _generate_meta({"href": favicon}) + "\n"
    else:
        logger.warning(
            """
            Invalid config value for favicon extension. Favicons will not be
            included in build.
            """)
        return None

    logger.info("++ META:")
    logger.info(meta_favicons)

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

    ###
    # logger.info("Extension running!")
    ###

    app.connect("html-page-context", html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
