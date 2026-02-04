"""Configuration fixtures of the tests (compatible with modern Sphinx)."""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup
import re

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir() -> Path:
    """The root directory for Sphinx test roots."""
    return Path(__file__).resolve().parent / "roots"


@pytest.fixture(autouse=True)
def _stub_network_for_images(monkeypatch):
    """Stub sphinx_favicon.requests.get to avoid network access during tests.

    Returns minimal GIF bytes with the requested dimensions parsed from the URL
    (e.g., "...16x16..." -> 16x16). Defaults to 16x16 if not found.
    """

    def _gif_bytes(w: int, h: int) -> bytes:
        # Minimal GIF header: "GIF89a" + width + height (little-endian) + 3 padding bytes
        return b"GIF89a" + int(w).to_bytes(2, "little") + int(h).to_bytes(2, "little") + b"\x00\x00\x00"

    def fake_get(url: str, *args, **kwargs):
        m = re.search(r"(\d+)x(\d+)", url)
        if m:
            w, h = int(m.group(1)), int(m.group(2))
        else:
            # Sensible default for URLs without size hint; tests don't assert these sizes
            w, h = 16, 16

        class _Resp:
            status_code = 200
            content = _gif_bytes(w, h)

        return _Resp()

    monkeypatch.setattr("sphinx_favicon.requests.get", fake_get)


@pytest.fixture()
def content(app):
    """The app build content."""
    app.build()
    yield app


def _link_tags(content, page):
    """Link tags in a page content."""
    c = (Path(content.outdir) / page).read_text()
    return BeautifulSoup(c, "html.parser").find_all("link")


def _favicon_tags(content, page="index.html"):
    """Favicon tags in the index.html page."""
    return [
        tag
        for tag in _link_tags(content, page)
        if tag.get("type", "").startswith("image")
    ]


def _meta_tags(content, page):
    """Link tags in a page content."""
    c = (Path(content.outdir) / page).read_text()
    return BeautifulSoup(c, "html.parser").find_all("meta")


@pytest.fixture()
def link_tags(content):
    """Link tags in index.html page."""
    return _link_tags(content, "index.html")


@pytest.fixture()
def meta_tags(content):
    """Meta tags in index.html page."""
    return _meta_tags(content, "index.html")


@pytest.fixture()
def favicon_tags(content):
    """Favicon tags in index.html page."""
    return _favicon_tags(content)


@pytest.fixture()
def favicon_tags_for_nested(content):
    """Favicon tags in nested/page.html page."""
    return _favicon_tags(content, "nested/page.html")


def pytest_configure(config):
    """Add markers config to pytest."""
    config.addinivalue_line("markers", "sphinx")
