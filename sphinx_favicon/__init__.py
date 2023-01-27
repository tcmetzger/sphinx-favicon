"""Sphinx extension to add custom favicons.

With sphinx-favicon, you can add custom favicons to your Sphinx html documentation quickly and easily.

You can define favicons directly in your conf.py, with different rel attributes such as "icon" or "apple-touch-icon" and any favicon size.

The sphinx-favicon extension gives you more flexibility than the standard favicon.ico supported by Sphinx. It provides a quick and easy way to add the most important favicon formats for different browsers and devices.
"""

from io import BytesIO
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union
from urllib.parse import urlparse

import docutils.nodes as nodes
import imagesize
import requests
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

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
        Favicon link or meta tag
    """
    # get the tag of the output
    tag = "meta" if "name" in favicon else "link"

    # default to "icon" for link elements
    if tag == "link":
        favicon.setdefault("rel", "icon")
        favicon["href"]  # to raise an error if not set
        extention = favicon["href"].split(".")[-1]

    # set the type for link elements.
    # if type is not set try to guess it from the file extention
    type_ = favicon.get("type")
    if not type_ and tag == "link" and extention in SUPPORTED_MIME_TYPES.keys():
        type_ = SUPPORTED_MIME_TYPES[extention]
        favicon["type"] = type_

    # build the html element
    parameters = [f'{k}="{v}"' for k, v in favicon.items() if v is not None]
    html_element = f"    <{tag} {' '.join(parameters)}>"

    return html_element


def _size(
    favicon: Dict[str, str], static_path: List[str], confdir: str
) -> Dict[str, str]:
    """Compute the size of the favicon if needed.

    If the file is a SUPPORTED_MIME_TYPES, then the size is computed on the fly and added
    to the favicon attributes. Don't do anything if the favicon is not a link tag

    Args:
        favicon: The favicon description as set in the conf.py file
        static_path: the static_path registered in the application
        confdir: the source directory of the documentation

    Returns:
        The favicon with a fully qualified size
    """
    # exit if the favicon tag has no href (like meta)
    if not (FILE_FIELD in favicon or "href" in favicon):
        return favicon

    # init the parameters
    link = favicon.get("href") or favicon.get(FILE_FIELD)
    extention = link.split(".")[-1]
    size = favicon.get("size")

    # get the size automatically if needed
    if size is None and extention in SUPPORTED_MIME_TYPES.keys():
        file = None
        if bool(urlparse(link).netloc):
            response = requests.get(link)
            if response.status_code == 200:
                file = BytesIO(response.content)
            else:
                logger.warn(
                    f"The provided link ({link}) cannot be read. "
                    "Size will not be computed."
                )
        else:
            for folder in static_path:
                path = Path(confdir) / folder / link
                if path.is_file():
                    file = path
                    break
            if file is None:
                logger.warn(
                    f"The provided path ({link}) is not part of any of the static path. "
                    "Size will not be computed."
                )

        # compute the image if a file have been set
        if file is not None:
            w, h = imagesize.get(file)
            size = f"{int(w)}x{int(h)}"
            favicon["size"] = size

    return favicon


def _static_to_href(pathto: Callable, favicon: Dict[str, str]) -> Dict[str, str]:
    """Replace static ref to fully qualified href.

    if the ``href`` is a relative path then it's replaced with the correct ``href``. We keep checking for ``static-file`` for legacy reasons.
    If both ``static-file`` and ``href`` are provided, ``href`` will be ignored.
    If the favicon has no ``href`` nor ``static-file`` then do nothing.

    Args:
        pathto: Sphinx helper_ function to handle relative URLs
        favicon: The favicon description as set in the conf.py file

    Returns:
        The favicon with a fully qualified href
    """
    # exit if the favicon tag has no href (like meta)
    if not (FILE_FIELD in favicon or "href" in favicon):
        return favicon

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


def create_favicons_meta(
    pathto: Callable, favicons: FaviconsDef, static_path: List[str], confdir: str
) -> Optional[str]:
    """Create ``<link>`` elements for favicons defined in configuration.

    Args:
        pathto: Sphinx helper_ function to handle relative URLs
        favicons: Favicon data from configuration. Can be a single dict or a list of dicts.
        static_path: the static_path registered in the application
        confdir: the source directory of the documentation

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

        if not isinstance(favicon, dict):
            logger.warning(
                f"Invalid config value for favicon extension: {favicon}."
                "Custom favicons will not be included in build."
            )
            continue
        tag = generate_meta(
            _static_to_href(pathto, _size(favicon, static_path, confdir))
        )
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
        favicons_meta = create_favicons_meta(
            pathto, app.config["favicons"], app.config["html_static_path"], app.confdir
        )
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
