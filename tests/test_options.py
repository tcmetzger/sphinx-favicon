"""Test suite for the sphinx-favicon extension."""

from itertools import chain
from pathlib import Path

import pytest


@pytest.mark.sphinx("html", testroot="list_of_three_dicts")
def test_list_of_three_dicts(favicon_tags):
    """Run tests on a list of 3 dicts.

    Args:
        favicon_tags: Favicon tags in index.html page.
    """
    # this test should have 3 favicons
    assert len(favicon_tags) == 3

    # all favicons should have rel, href, type, and sizes attributes
    for favicon_tag in favicon_tags:
        assert favicon_tag["rel"]
        assert favicon_tag["href"]
        assert favicon_tag["type"]
        assert favicon_tag["sizes"]

    # check first favicon in more detail
    assert favicon_tags[0]["rel"] == ["icon"]
    assert (
        favicon_tags[0]["href"]
        == "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-16x16.png"
    )
    assert favicon_tags[0]["type"] == "image/png"
    assert favicon_tags[0]["sizes"] == "16x16"


@pytest.mark.sphinx("html", testroot="list_of_three_icons_automated_values")
def test_list_of_three_icons_automated_values(favicon_tags):
    """Run tests on a list of 3 dicts with automated values.

    Args:
        favicon_tags: Favicon tags in index.html page.
    """
    # this test should have 3 favicons
    assert len(favicon_tags) == 3

    # all favicons should have rel, href, type, and sizes attributes
    for favicon_tag in favicon_tags:
        assert favicon_tag["rel"]
        assert favicon_tag["href"]
        assert favicon_tag["type"]
        assert favicon_tag["sizes"]

    # check first favicon in more detail
    assert favicon_tags[0]["rel"] == ["icon"]
    assert (
        favicon_tags[0]["href"]
        == "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/favicon-16x16.png"
    )
    assert favicon_tags[0]["type"] == "image/png"
    assert favicon_tags[0]["sizes"] == "16x16"


@pytest.mark.sphinx("html", testroot="single_dict")
def test_single_dict(favicon_tags):
    """Run tests on a single dict.

    Args:
        favicon_tags: Favicon tags in index.html page.
    """
    # this test should have 1 favicon
    assert len(favicon_tags) == 1

    # check favicon
    assert favicon_tags[0]["rel"] == ["apple-touch-icon"]
    assert (
        favicon_tags[0]["href"]
        == "https://raw.githubusercontent.com/tcmetzger/sphinx-favicon/main/docs/source/_static/apple-touch-icon.png"
    )
    assert favicon_tags[0]["type"] == "image/png"
    assert favicon_tags[0]["sizes"] == "180x180"


@pytest.mark.sphinx("html", testroot="list_of_urls")
def test_list_of_urls(favicon_tags):
    """Run tests on a list of urls.

    Args:
        favicon_tags: Favicon tags in index.html page.
    """
    # this test should have 3 favicons
    assert len(favicon_tags) == 3

    # all favicons should have rel, href, and type attributes
    for favicon_tag in favicon_tags:
        assert favicon_tag["rel"]
        assert favicon_tag["href"]
        assert favicon_tag["type"]

    # check first favicon in more detail
    assert favicon_tags[0]["rel"] == ["icon"]
    assert (
        favicon_tags[0]["href"]
        == "https://secure.example.com/favicon/favicon-16x16.gif"
    )
    assert favicon_tags[0]["type"] == "image/gif"


@pytest.mark.sphinx("html", testroot="static_files")
def test_static_files(app, favicon_tags, favicon_tags_for_nested):
    """Run tests using static files.

    Args:
        app: the Sphinx application
        favicon_tags: Favicon tags in index.html page.
        favicon_tags_for_nested: Favicon tags in nested/page.html page.
    """
    # this test should have 2 favicons
    assert len(favicon_tags) == 3

    # all favicons should have rel, href, and type attributes
    for favicon_tag in chain(favicon_tags, favicon_tags_for_nested):
        assert favicon_tag["rel"] == ["icon"]
        assert "_static" in favicon_tag["href"]
        assert favicon_tag["type"] == "image/svg+xml"
        assert "static-file" not in favicon_tag

    for favicon_tag in favicon_tags:
        assert favicon_tag["href"].startswith("_static")

    for favicon_tag in favicon_tags_for_nested:
        assert favicon_tag["href"].startswith("../_static")

    static = Path(app.outdir, "_static")
    assert (static / "square.svg").exists()
    assert (static / "nested/triangle.svg").exists()
    assert (static / "circle.svg").exists()


@pytest.mark.sphinx("html", testroot="href_and_static")
def test_href_and_static(app, favicon_tags, favicon_tags_for_nested):
    """Run tests on a mix of static files and complete urls.

    Args:
        app: the Sphinx application
        favicon_tags: Favicon tags in index.html page.
        favicon_tags_for_nested: Favicon tags in nested/page.html page.
    """
    # this test should have 3 favicons
    assert len(favicon_tags) == 2

    # all favicons should have rel, href, type, and sizes attributes
    for favicon_tag in chain(favicon_tags, favicon_tags_for_nested):
        assert favicon_tag["rel"] == ["icon"]
        assert "_static" in favicon_tag["href"]
        assert favicon_tag["type"] == "image/svg+xml"
        assert favicon_tag["sizes"]
        assert "static-file" not in favicon_tag

    for favicon_tag in favicon_tags:
        assert favicon_tag["href"].startswith("_static")

    for favicon_tag in favicon_tags_for_nested:
        assert favicon_tag["href"].startswith("../_static")

    # favicons should use relative paths, ignoring paths provided with `href`
    static = Path(app.outdir, "_static")
    assert (static / "square.svg").exists()
    assert (static / "nested/triangle.svg").exists()


@pytest.mark.sphinx("html", testroot="msapp_meta")
def test_msapp_meta(favicon_tags, meta_tags):
    """Run tests on a favicon configuration with meta.

    Args:
        favicon_tags: Favicon tags in index.html page.
        meta_tags: Meta tags in index.html page.
    """
    # this test should have 1 link tag
    assert len(favicon_tags) == 1

    # get all values from meta tags and check for expected values
    tag_values = []
    for tag in meta_tags:
        tag_values.extend(list(tag.attrs.values()))
    assert "msapplication-TileColor" in tag_values
    assert "#2d89ef" in tag_values
    assert "theme-color" in tag_values
    assert "#ffffff" in tag_values
