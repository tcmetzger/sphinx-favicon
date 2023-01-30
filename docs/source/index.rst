Sphinx Favicon
==============

**A Sphinx extension to add custom favicons**

With **sphinx-favicon**, you can add custom favicons to your Sphinx HTML documentation quickly and easily.

You can define favicons directly in your ``conf.py``, with any attributes (``rel``, ``size``, ``href``, ``name``...) and they will be transformed into ``<link>`` OR ``<meta>`` tags in your html output.

The **sphinx-favicon** extension gives you more flexibility than the `standard "favicon.ico" supported by Sphinx <https://www.sphinx-doc.org/en/master/templating.html?highlight=favicon#favicon_url>`__. It provides a quick and easy way to add the most important favicon formats for different browsers and devices.

Installation
------------

Use ``pip`` to install **sphinx-favicon** in your environment:

.. code-block:: console
   
   pip install sphinx-favicon


Usage
-----

Enable the extention 
^^^^^^^^^^^^^^^^^^^^

After installing **sphinx-favicon**, you can configure the extension directly in `conf.py` by addding ``sphinx_favicon`` to the list of extentions:

.. code-block:: python

   extensions = [
      #[...]
      "sphinx_favicon",
   ]

Add favicons
^^^^^^^^^^^^

A favicon is described as a dictionary of *HTML attribute name*. There are two ways to include favicon files in your configuration using the ``favicons`` configuration in your ``conf.py``:

-  provide a single favicon to get the following ``<link>`` in the HTML ``<head>``:

   .. code-block:: python 
      
      html_static_path = ["_static"]
      favicons = {"rel": "icon", "href": "icon.svg", "type": "image/svg+xml"}

   .. code-block:: html
      
      <link rel="icon" href="_static/icon.svg" type="image/svg+xml">

-  provide a list of favicon covering different platforms to get the following ``<link>`` (s) in the HTML ``<head>``:

   .. code-block:: python 
      
      html_static_path = ["_static"]
      favicons = [
         {"rel": "icon", "href": "icon.svg", "type": "image/svg+xml"},
         {"rel": "icon", "sizes": "16x16", "href": "favicon-16x16.png", "type": "image/png"},
         {"rel": "icon", "sizes": "32x32", "href": "favicon-32x32.png", "type": "image/png"},
         {"rel": "apple-touch-icon", "sizes": "180x180", "href": "apple-touch-icon-180x180.png" "type": "image/png"}
      ]

   .. code-block:: html
      
      <link rel="icon" href="_static/icon.svg" type="image/svg+xml">
      <link rel="icon" href="_static/favicon-16x16.png" sizes="16x16" type="image/png">
      <link rel="icon" href="_static/favicon-32x32.png" sizes="32x32" type="image/png">
      <link rel="apple-touch-icon" href="_static/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">

Minimal setup
^^^^^^^^^^^^^

The only information required to define a favicon is the image url, relative to ``_static`` or absolute. Then if the favicon is only relying on default parameters (a ``<link>`` with ``rel="icon"`` using a standard mime type) the dictionnary can be replaced by a string corresponding to the ``href`` attribute. 

The initial example can thus be reduced to a single string and/or a list of string: 

-  provide a single favicon to get the following ``<link>`` in the HTML ``<head>``:

   .. code-block:: python 
      
      html_static_path = ["_static"]
      favicons = "icon.svg"

   .. code-block:: html
      
      <link rel="icon" href="_static/icon.svg" type="image/svg+xml">

-  provide a list of favicon covering different platforms to get the following ``<link>`` (s) in the HTML ``<head>``:

   .. note:: 
      
      The "apple-touch-icon" cannot be reduced to a simple string as it's not a default ``rel``. More information in :ref:`Customization`.

   .. code-block:: python 
      
      html_static_path = ["_static"]
      favicons = [
         "icon.svg"
         "favicon-16x16.png",
         "favicon-32x32.png"
         {"rel": "apple-touch-icon", "href": "apple-touch-icon-180x180.png"}
      ]

   .. code-block:: html
      
      <link rel="icon" href="_static/icon.svg" type="image/svg+xml">
      <link rel="icon" href="_static/favicon-16x16.png" sizes="16x16" type="image/png">
      <link rel="icon" href="_static/favicon-32x32.png" sizes="32x32" type="image/png">
      <link rel="apple-touch-icon" href="_static/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">

Customization
^^^^^^^^^^^^^

You can use any parameters to define your favicon as long as they are interpreted by browsers. Some specific keywords will change the HTML content:

type of output
##############

**sphinx-favicon** will recognize the type of html tag required by looking at the attributes set in the favicon.

-  ``<link``: it's the default type of html favicon.
-  ``<meta>``: only used if ``name`` is set in the attributes. useful for msapp favicons.

location of the image 
#####################

You can set images in ``href`` attribute in 2 ways: 

-   Use an **absolute URL** for a favicon file.
-   Use a **local static file** as a favicon. Make sure you place your local static favicon file(s) inside a directory listed in Sphinx `"html_static_path" <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=static#confval-html_static_path>`__.

.. note:: 

   We continue to support the legacy ``static_file`` from v0.2 for local files.

size
####

a value for the favicon's ``sizes`` attribute as defined `here <https://html.spec.whatwg.org/multipage/semantics.html#attr-link-sizes>`__. It is computed on the fly if not set for "bmp", "gif", "jpeg", "jpg" and "png" extentions.

relation (``rel``)
##################

a value for the favicon's ``rel`` attribute, usually either the standard `icon <https://html.spec.whatwg.org/multipage/links.html#rel-icon>`__ or a custom extension like `apple-touch-icon <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`__. 

It is set to ``rel="icon"`` by default but can be set to other values depending on your need such as ``apple-touch-icon``.

type
####

a value specifying the favicon's MIME type as defined `here <https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type>`__. It is computed automatically if not set for "bmp", "gif", "ico", "jpeg", "jpg", "png" and "svg" extentions.

Contribute
----------

Thank you for your help improving **sphinx-favicon**!

**sphinx-favicon** uses `nox <https://nox.thea.codes/en/stable/>`__ to automate several
development-related tasks.
Currently, the project uses four automation processes (called sessions) in ``noxfile.py``:

-   ``mypy``: to perform a mypy check on the lib;
-   ``test``: to run the test with pytest;
-   ``docs``: to build the documentation in the ``build`` folder;
-   ``lint``: to run the pre-commits in an isolated environment

Every nox session is run in its own virtual environment, and the dependencies are
installed automatically.

To run a specific nox automation process, use the following command:

.. code-block:: console

   nox -s {{session name}}

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

First off, you'll need your own copy of the **sphinx-favicon** codebase. You can clone it for local development like so:

Fork the repository so you have your own copy on GitHub. See the `GitHub forking guide for more information <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`__. Then, clone the repository locally so that you have a local copy to work on:

.. code-block:: console

   git clone https://github.com/{{ YOUR USERNAME }}/sphinx-favicon
   cd sphinx-favicon

Then install the development version of the extention:

.. code-block:: console

   pip install -e .[dev]

This will install the sphinx-favicon library, together with two extra tools:
-   `pre-commit <https://pre-commit.com>`__ for automatically enforcing code standards and quality checks before commits.
-   `nox <https://nox.thea.codes/en/stable/>`__, for automating common development tasks.

Lastly, activate the pre-commit hooks by running:

.. code-block:: console

      pre-commit install

This will install the necessary dependencies to run pre-commit every time you make a commit with Git.

Contribute to the codebase
^^^^^^^^^^^^^^^^^^^^^^^^^^

Any larger updates to the codebase should include tests and documentation.
The tests are located in the ``tests`` folder, and the documentation is located in the ``docs`` folder.

To run the tests locally, use the following command:

.. code-block:: console

      nox -s test

See :ref:`below <contributing-docs>` for more information on how to update the documentation.

.. _contributing-docs:

Contribute to the docs
^^^^^^^^^^^^^^^^^^^^^^

The documentation is built using `Sphinx <https://www.sphinx-doc.org/en/master/>`__ and
deployed to `Read the Docs <https://readthedocs.org/>`__.

To build the documentation locally, use the following command:

.. code-block:: console

      nox -s docs


