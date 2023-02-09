Quickstart
==========

This section contains basic information about **Sphinx Favicon** to get you started.

Installation
------------

Use ``pip`` to install **Sphinx Favicon** in your environment:

.. code-block:: console

    pip install sphinx-favicon

Extension setup
---------------

Enable the extension
^^^^^^^^^^^^^^^^^^^^

After installing **Sphinx Favicon**, add ``sphinx_favicon`` to the list of extensions
in your ``conf.py`` file:

.. code-block:: python

    extensions = [
        #[...]
        "sphinx_favicon",
    ]

Check static directory configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case you want to use favicons from files in your static directory, make sure that
the `html_static_path <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path>`_
in your ``conf.py`` is configured correctly. For example:

.. code-block:: python

    html_static_path = ["_static"]

Favicon configuration
---------------------

Add basic favicons
^^^^^^^^^^^^^^^^^^

After adding ``sphinx_favicon`` to your list of extensions, you can now use the
``favicons`` variable in ``conf.py`` to define favicons.

There are many ways to define favicons, with varying degrees of complexity.
The simplest way to add favicons is to define a list of favicon file names or URLs.

For example:

.. code-block:: python

    favicons = [
        "favicon-16x16.png",
        "favicon-32x32.png",
        "icon.svg",
    ]

**Sphinx Favicon** automatically determines the relevant attributes for each favicon and
adjusts paths for static files where necessary.

Based on this configuration, **Sphinx Favicon** adds the following ``<link>`` tags in
the HTML ``<head>`` for each page in your Sphinx-generated HTML documentation:

.. code-block:: html

    <link href="_static/favicon-16x16.png" sizes="16x16" rel="icon" type="image/png">
    <link href="_static/favicon-32x32.png" sizes="32x32" rel="icon" type="image/png">
    <link href="_static/icon.ico" rel="icon" type="image/x-icon">

You can mix file names (relative to your ``html_static_path``) and URLs in this list.
For example:

.. code-block:: python

    favicons = [
        "https://picsum.photos/16/16",
        "https://picsum.photos/32/32",
    ]

This will add the following ``<link>`` tags:

.. code-block:: html

    <link href="https://picsum.photos/16/16" sizes="16x16" rel="icon" type="image/png">
    <link href="https://picsum.photos/32/32" sizes="32x32" rel="icon" type="image/png">

Advanced usage
--------------

This chapter only covers basic setup. For more advanced usage, see the
:ref:`following chapter <configuration>`!
