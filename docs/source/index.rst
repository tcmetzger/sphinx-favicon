Sphinx Favicon
==============

**A Sphinx extension to add custom favicons**

With **sphinx-favicon**, you can add custom favicons to your Sphinx html documentation quickly and easily.

You can define favicons directly in your `conf.py`, with different `rel` attributes such as `"icon" <https://html.spec.whatwg.org/multipage/links.html#rel-icon>`__ or `"apple-touch-icon" <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`__ and any favicon size.

The **sphinx-favicon** extension gives you more flexibility than the `standard "favicon.ico" supported by Sphinx <https://www.sphinx-doc.org/en/master/templating.html?highlight=favicon#favicon_url>`__. It provides a quick and easy way to add the most important favicon formats for different browsers and devices.

Installation
------------

Use ``pip`` to install **sphinx-favicon** in your environment:

.. code-block:: console
   
   pip install sphinx-favicon


Usage
-----

After installing **sphinx-favicon**, you can configure the extension directly in `conf.py`. There are two ways to include favicon files in your configuration:

-   Use an **absolute URL** for a favicon file (beginning with ``http://`` or ``https://``). If you use an absolute URL, use the ``href`` parameter.
-   Use a **local static file** as a favicon. Make sure you place your local static favicon file(s) inside a directory listed in `Sphinx "html_static_path" <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path>`__. To use a relative path, use the ``static-file`` parameter.

To configure **sphinx-favicon**, first add ``sphinx_favicon`` to the list of extensions:

.. code-block:: python

   extensions = [
      #[...]
      "sphinx_favicon",
   ]

Several options are then available to define favicons. They are listed in the following sections.

Provide detailed metadata as a list of dicts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use a list of dicts for maximum control over the favicons added to your html document. You can use any parameters to define your favicon as long as they are interpreted by browsers. Some specific keyword will change the exported html content:

-   ``rel``: a value for the favicon's ``rel`` attribute, usually either the standard `icon <https://html.spec.whatwg.org/multipage/links.html#rel-icon>`__ or a custom extension like `apple-touch-icon <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`__.
-   ``sizes``: a value for the favicon's ``sizes`` attribute as defined `here <https://html.spec.whatwg.org/multipage/semantics.html#attr-link-sizes>`__. It is computed on the fly using if not set.
-   ``type``: a value specifying the favicon's MIME type as defined `here <https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type>`__. It is computed on the fly of not set.
-   ``href``: the **absolute URL** to the favicon's image file (not required if you use the ``static-file`` parameter)
-   ``static-file``: the **local static file** corresponding to your icon's image. Please notice this path should be relative to a directory listed in `Sphinx "html_static_path" <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path>`__ (usually ``_static``). If you define both ``static-file`` and ``href``, the value for ``href`` will be ignored.
-   ``name``: a value for the favicon's ``name``. Usually set for microsoft app metadata. If set the tag will be set to ``meta``.

**Example**

.. code-block:: python
   
   html_static_path = ["_static"]  # html_static_path is required if you use the "static-file" parameter

   favicons = [
      {
         "rel": "icon",
         "static-file": "icon.svg",  # => use `_static/icon.svg`
         "type": "image/svg+xml",
      },
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "https://secure.example.com/favicon/favicon-16x16.png",
         "type": "image/png",
      },
      {
         "rel": "icon",
         "sizes": "32x32",
         "href": "https://secure.example.com/favicon/favicon-32x32.png",
         "type": "image/png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "180x180",
         "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
         "type": "image/png",
      },
   ]

Based on this configuration, Sphinx will include the following favicon information in the HTML `<head>` element:

.. code-block:: html

   <link rel="icon" href="_static/icon.svg" type="image/svg+xml">
   <link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.png" sizes="16x16" type="image/png">
   <link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" sizes="32x32" type="image/png">
   <link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">

Note that the relative path to the favicon's image file in the static directory will be adjusted according to each html file's location.

To make things easier for you, **sphinx-favicon** can also add *some* metadata to each favicon's `<link>` element automatically:

-   If you don't provide the ``rel`` argument, **sphinx-favicon** automatically adds ``rel="icon"`` for ``link`` tags.
-   if you don't provide the ``type`` argument, **sphinx-favicon** automatically determines the MIME type based on the image's filename extension.
-   If not provided, **sphinx-favicon** will compute the ``size`` arguments automatically from the image provided in ``href``.

Therefore, the following simplified configuration generates the exact same HTML result as above:

.. code-block:: python

   html_static_path = ["_static"]

   favicons = [
      {"static-file": "icon.svg"},  # => use `_static/icon.svg`
      {"href": "https://secure.example.com/favicon/favicon-16x16.png"},
      {"href": "https://secure.example.com/favicon/favicon-32x32.png"},
      {
         "rel": "apple-touch-icon",
         "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
      },
   ]

Provide a single dict for just one favicon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to add just one custom favicon, you can also use a simple dict in ``conf.py``:

.. code-block:: python

   favicons = {
      "rel": "apple-touch-icon",
      "sizes": "180x180",
      "href": "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
   }

Based on this configuration, Sphinx will include the following favicon information in the ``<head>`` of every HTML file:

.. code-block:: html
   
   <link rel="apple-touch-icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">

Provide a list of local favicon files or URLs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The quickest way to add favicons is just adding a list of favicon URLs to ``conf.py``.

.. code-block:: python

   html_static_path = ["_static"]
   favicons = [
      "icon.svg",  # => `_static_/icon.svg`
      "https://secure.example.com/favicon/favicon-16x16.gif",
      "https://secure.example.com/favicon/favicon-32x32.png",
      "https://secure.example.com/favicon/apple-touch-icon-180x180.png",
   ]

Based on this configuration, Sphinx will include the following favicon information in the HTML ``<head>`` element:

.. code-block:: html

   <link rel="icon" href="_static/icon.svg" type="image/svg+xml">
   <link rel="icon" href="https://secure.example.com/favicon/favicon-16x16.gif" type="image/gif">
   <link rel="icon" href="https://secure.example.com/favicon/favicon-32x32.png" type="image/png">
   <link rel="icon" href="https://secure.example.com/favicon/apple-touch-icon-180x180.png" type="image/png">

Please note that if your URLs don't start with ``https://``, ``http://`` or ``/``, they will be considered a static file inside a directory listed in `Sphinx "html_static_path" <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path>`__.

Contribute
----------

Workflow for contributing changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We follow a typical GitHub workflow of:

-   Create a personal fork of this repo
-   Create a branch
-   Open a pull request
-   Fix findings of various linters and checks
-   Work through code review

For each pull request, the documentation is built and deployed to make it easier to review the changes in the PR. To access this, click on the Read the Docs preview in the CI/CD jobs.

.. note:: 
   
   The sections below cover the steps to do this in more detail.

Clone the repository
^^^^^^^^^^^^^^^^^^^^

First off you’ll need your own copy of the **sphinx-favicon** codebase. You can clone it for local development like so:

Fork the repository so you have your own copy on GitHub. See the `GitHub forking guide for more information <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`__. Then, clone the repository locally so that you have a local copy to work from:

.. code-block:: console

   git clone https://github.com/{{ YOUR USERNAME }}/sphinx-favicon
   cd sphinx-favicon

Then install the development version of the extention:

.. code-block:: console

   pip install -e .[dev]

This will install the lib and 2 extra tools:
-   `pre-commit <https://pre-commit.com>`__ for automatically enforcing code standards and quality checks before commits.
-   `nox <https://nox.thea.codes/en/stable/>`__, for automating common development tasks.

Lastly activate the pre-commit hooks by running: 

.. code-block:: console

      pre-commit install


This will install the necessary dependencies to run pre-commit every time you make a commit with Git.

Run nox automation
^^^^^^^^^^^^^^^^^^

**sphinx-favicon** embed 4 automation process (called sessions) in ``noxfile.py``:

-   ``mypy``: to perform a mypy check on the lib;
-   ``test``: to run the test with pytest;
-   ``docs``: to build the documentation in the ``build`` folder;
-   ``lint``: to run the pre-commits in an isolated environment

To run nox automation process navigate to the extention folder and run the following:

.. code-block:: console

   nox -s {{session name}}
