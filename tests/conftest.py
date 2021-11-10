import os
import pytest
from bs4 import BeautifulSoup
from sphinx.testing.path import path

# from sphinx.application import Sphinx

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture
def srcdir(app):
    return path(app.srcdir)


@pytest.fixture
def shareddir(srcdir, rootdir):
    dirpath = srcdir.parent / "shared"
    if not dirpath.exists():
        (rootdir / "shared").copytree(dirpath)
    return dirpath


@pytest.fixture()
def content(app, shareddir):
    # meta tests to make sure test setup is correct
    assert shareddir.exists()
    assert shareddir == app.srcdir.parent / "shared"
    assert len(shareddir.listdir()) > 0

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
    # return [
    #     tag for tag in _link_tags(content) if tag.get("type", "").startswith("image")
    # ]


@pytest.fixture()
def favicon_tags_for_nested(content):
    return _favicon_tags(content, "nested/page.html")


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
