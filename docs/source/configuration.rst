Configuration
=============

In the quickstart guide, you have used a simple list of favicons and **Sphinx Favicon**
has automatically generated the corresponding HTML tags.

This section will explain how to customize the configuration and use specific tags and
attributes such as ``apple-touch-icon``.

Defining favicons
^^^^^^^^^^^^^^^^^

Every favicon in **Sphinx Favicon** is defined as a dictionary of HTML attributes.

For a single favicon, you can provide a single dictionary:

.. code-block:: python

   favicons = {"rel": "icon", "href": "icon.svg", "type": "image/svg+xml"}

This will generate the following HTML tag:

.. code-block:: html

   <link rel="icon" href="_static/icon.svg" type="image/svg+xml">

For multiple favicons, provide a list of dictionaries:

.. code-block:: python

   favicons = [
      {"rel": "icon", "href": "icon.svg", "type": "image/svg+xml"},
      {"rel": "icon", "sizes": "16x16", "href": "favicon-16x16.png", "type": "image/png"},
      {"rel": "icon", "sizes": "32x32", "href": "favicon-32x32.png", "type": "image/png"},
      {"rel": "apple-touch-icon", "sizes": "180x180", "href": "apple-touch-icon-180x180.png" "type": "image/png"}
   ]

This will generate the following HTML tags:

.. code-block:: html

   <link rel="icon" href="_static/icon.svg" type="image/svg+xml">
   <link rel="icon" href="_static/favicon-16x16.png" sizes="16x16" type="image/png">
   <link rel="icon" href="_static/favicon-32x32.png" sizes="32x32" type="image/png">
   <link rel="apple-touch-icon" href="_static/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">

For any attributes that you don't explicitly set, **Sphinx Favicon** will infer the
values from your provided input. For example: if you don't provide a ``type`` attribute,
**Sphinx Favicon** will infer the type from the file extension. If you don't provide a
``sizes`` attribute, **Sphinx Favicon** will attempt to read the pixel dimensions of the
provided image.

.. note::

   If you provide a simple list (like in the quickstart guide), **Sphinx Favicon** will
   automatically generate the dict behind the scenes.

   Your list of favicons can also be a mixture of strings and dicts:

   .. code-block:: python

      favicons = [
         "icon.svg",
         "favicon-32x32.png",
         {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
      ]

   This will generate the following HTML tags:

   .. code-block:: html

      <link href="_static/icon.svg" rel="icon" type="image/svg+xml">
      <link href="_static/favicon-32x32.png" sizes="32x32" rel="icon" type="image/png">
      <link rel="apple-touch-icon" href="_static/_static/_static/apple-touch-icon.png" sizes="180x180" type="image/png">

Customization
^^^^^^^^^^^^^

You can use any parameters to define your favicon as long as they are interpreted by
browsers.

The following attributes are the most commonly used ones:

``href``: the image location
############################

You can define favicon images with the ``href`` attribute in two ways:

- Use an **absolute URL** for a favicon file. For example:
   ``"href": "https://www.sphinx-doc.org/en/master/_static/favicon.svg"``.
- Use a **local static file** as a favicon. Make sure you place your local static
   favicon file(s) inside a directory listed in the Sphinx
   `"html_static_path" <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path>`__.
   For example: ``"href": "favicon.svg"``.

.. note:: 

   We continue to support the legacy ``static_file`` from v0.2 for local files.

``sizes``: the image size
#########################

Use the ``sizes`` attribute as defined
`here <https://html.spec.whatwg.org/multipage/semantics.html#attr-link-sizes>`__.

For example: ``"sizes": "16x16"``.

**Sphinx Favicon** automatically computes a favicon's size if you don't provide a
value for the ``sizes`` attribute (for BMP, GIF, JPEG, JPG and PNG files).

``rel``: the favicon relation
#############################

Use the ``rel`` attribute to define the favicon relation. This can either be the
standard `"icon" and "shortcut icon" <https://html.spec.whatwg.org/multipage/links.html#rel-icon>`__,
or a custom relation like
`"apple-touch-icon" <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`__.

If you don't provide a value for the ``rel`` attribute, **Sphinx Favicon** will
automatically set ``rel="icon"``.

``type``: the image MIME type
#############################

Use the ``type`` to define a favicon's MIME type as defined
`here <https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type>`__.

If you don't provide a value for the ``rel`` attribute, **Sphinx Favicon** will
automatically extract the MIME type from the provided image file  (for BMP, GIF, ICO,
JPEG, JPG, PNG, and SVG files).

``name``: specific to msapp icons
#################################

You also have the option to specify a ``name`` attribute. This is useful for
``msapplication``-style favicons.

If you use the ``name`` attribute, **Sphinx Favicon** will automatically set the
``rel`` attribute to ``"meta"``.

For example:

   .. code-block:: python

      favicons = [
         "mstile-150x150.png",
         {"name": "msapplication-TileColor", "content": "#2d89ef"},
         {"name": "theme-color", "content": "#ffffff"},
      ]

This will generate the following HTML tags:

.. code-block:: html

   <link href="_static/mstile-150x150.png" sizes="150x150" rel="icon" type="image/png">
   <meta name="msapplication-TileColor" content="#2d89ef">
   <meta name="theme-color" content="#ffffff">

.. tip::

   See the ``conf.py`` file for this documentation in the project's GitHub repository,
   at https://github.com/tcmetzger/sphinx-favicon/blob/main/docs/source/conf.py
