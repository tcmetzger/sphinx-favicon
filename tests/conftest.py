import os
import pytest
from bs4 import BeautifulSoup
from sphinx.testing.path import path

# from sphinx.application import Sphinx

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture()
def content(app):
    app.build()
    yield app


def _link_tags(content, page):
    c = (content.outdir / page).read_text()
    return BeautifulSoup(c, "html.parser").find_all("link")


def _favicon_tags(content, page="index.html"):
    return [
        tag
        for tag in _link_tags(content, page)
        if tag.get("type", "").startswith("image")
    ]


@pytest.fixture()
def link_tags(content):
    return _link_tags(content, "index.html")


@pytest.fixture()
def favicon_tags(content):
    return _favicon_tags(content)


@pytest.fixture()
def favicon_tags_for_nested(content):
    return _favicon_tags(content, "nested/page.html")


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
