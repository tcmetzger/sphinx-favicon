from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union

import docutils.nodes as nodes
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.fileutil import copy_asset_file

logger = logging.getLogger(__name__)

PUBLIC_IMAGES_DIR = "_images"  # Same directory used by .. image::
ABSOLUTE_HREF_STARTERS = ("https://", "http://", "/")
FaviconsDef = Union[Dict[str, str], List[Dict[str, str]]]

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


class FaviconMetadata:
    """Generate favicon metadata tags, that can be inserted in the ``<head>``
    of a HTTP document.

    Args:
        app (Sphinx): Sphinx application (as passed to a event_ handler)
        context (dict): Sphinx context (as passed to a event_ handler)
        images_dir (str): Name of the directory where images will be
            copied to (e.g. ``_images``).
        favicons (FaviconsDef): Favicon data from configuration.
            Can be a single dict or a list of dicts.

    .. _event: https://www.sphinx-doc.org/en/master/extdev/appapi.html#events
    """

    def __init__(
        self,
        app: Sphinx,
        context: Dict[str, Any],
        images_dir: str,
        favicons: FaviconsDef,
    ) -> None:
        self.srcdir = Path(app.srcdir)
        self.confdir = Path(app.confdir)
        self.images_dir = Path(app.builder.outdir, images_dir)
        self.favicons: FaviconsDef = favicons
        try:
            self.pathto: Callable = context["pathto"]  # Sphinx helper to resolve paths
        except KeyError as ex:
            msg = "sphinx-favicon needs to be used in an HTML context"
            raise ValueError(msg) from ex

    def _find_file(self, file: str) -> Path:
        candidates = [self.confdir / file, self.srcdir / file]
        path = next((x for x in candidates if x.is_file()), None)
        if path is None:
            raise FileNotFoundError(f"{file!r} not found, trying {candidates!r}")
        return path

    def _local_to_href(self, favicon: Dict[str, str]) -> Dict[str, str]:
        """Copy icon-related files to the ``PUBLIC_IMAGES_DIR`` and return a modified
        version of the icon attributes replacing ``file`` with the correct ``href``.
        """
        if "file" in favicon:
            src = self._find_file(favicon["file"])
            copy_asset_file(str(src), str(self.images_dir))
            href = Path(self.images_dir.name, src.name)
            attrs = favicon.copy()
            attrs.pop("file")
            attrs["href"] = str(self.pathto(str(href), resource=True))
            return attrs

    def __call__(self) -> Optional[str]:
        """Create ``<link>`` elements for the given favicons.

        Returns:
            str: ``<link>`` elements for all favicons.
        """

        favicons = self.favicons
        meta_favicons = ""

        # generate meta for favicon dict
        if isinstance(favicons, dict):
            meta_favicons += generate_meta(self._local_to_href(favicons))
        # generate meta for list of favicon dicts
        elif isinstance(favicons, list) and isinstance(favicons[0], dict):
            for favicon in favicons:
                meta_favicons += generate_meta(self._local_to_href(favicon)) + "\n"
        # generate meta for list of favicon URLs
        elif isinstance(favicons, list):
            for favicon in favicons:
                if any(favicon.startswith(x) for x in ABSOLUTE_HREF_STARTERS):
                    attrs = {"href": favicon}
                else:
                    attrs = self._local_to_href({"file": favicon})
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

    favicons_meta = None

    if doctree and app.config["favicons"]:
        defs = app.confdir["favicons"]
        favicons_meta = FaviconMetadata(app, context, PUBLIC_IMAGES_DIR, defs)
        context["metatags"] += favicons_meta()


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("favicons", None, "html")

    image_dir = Path(app.outdir, PUBLIC_IMAGES_DIR)
    image_dir.mkdir(exist_ok=True)

    app.connect("html-page-context", html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
