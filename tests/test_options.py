from itertools import chain
from pathlib import Path

import pytest

@pytest.mark.sphinx("html", testroot="list_of_three_dicts")
def test_list_of_three_dicts(favicon_tags):

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
        == "https://secure.example.com/favicon/favicon-16x16.png"
    )
    assert favicon_tags[0]["type"] == "image/png"
    assert favicon_tags[0]["sizes"] == "16x16"


@pytest.mark.sphinx("html", testroot="list_of_three_dicts_automated_values")
def test_list_of_three_dicts_automated_values(favicon_tags):

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
        == "https://secure.example.com/favicon/favicon-16x16.png"
    )
    assert favicon_tags[0]["type"] == "image/png"
    assert favicon_tags[0]["sizes"] == "16x16"


@pytest.mark.sphinx("html", testroot="single_dict")
def test_single_dict(favicon_tags):

    # this test should have 1 favicon
    assert len(favicon_tags) == 1

    # check favicon
    assert favicon_tags[0]["rel"] == ["apple-touch-icon"]
    assert (
        favicon_tags[0]["href"]
        == "https://secure.example.com/favicon/apple-touch-icon-180x180.png"
    )
    assert favicon_tags[0]["type"] == "image/png"
    assert favicon_tags[0]["sizes"] == "180x180"


@pytest.mark.sphinx("html", testroot="list_of_urls")
def test_list_of_urls(favicon_tags):

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

    # this test should have 2 favicons
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

    static = Path(app.outdir, "_static")
    assert (static / "square.svg").exists()
    assert (static / "nested/triangle.svg").exists()


@pytest.mark.sphinx("html", testroot="href_and_static")
def test_href_and_static(app, favicon_tags, favicon_tags_for_nested):

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
