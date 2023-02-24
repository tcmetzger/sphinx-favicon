"""Configuration fixtures of the tests."""

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    """The root directory."""
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture()
def content(app):
    """The app build content."""
    app.build()
    yield app


def _link_tags(content, page):
    """Link tags in a page content."""
    c = (content.outdir / page).read_text()
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
    c = (content.outdir / page).read_text()
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
