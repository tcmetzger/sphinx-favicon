Sphinx Favicon
==============

**A Sphinx extension to add custom favicons**

With **Sphinx Favicon**, you can add custom favicons to your Sphinx HTML documentation.

You can define favicons directly in your ``conf.py``, using attributes such as ``rel``,
``sizes``, ``href``, or ``name``. **Sphinx Favicon** creates the respective ``<link>``
or ``<meta>`` tags in your HTML output.

The **Sphinx Favicon** extension gives you more flexibility than the
`standard "favicon.ico" supported by Sphinx <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon>`_.
**Sphinx Favicon** provides a quick and easy way to add the most important favicon
formats for different browsers and devices.

For example, you can add support for general as well as vendor-specific favicons,
including ``apple-touch-icon`` and ``mask-icon``. See our
:ref:`quickstart guide <quickstart>` to get started!

Documentation contents
----------------------

This documentation contains three sections:

.. grid:: 1 1 3 3

   .. grid-item-card::
      :link: quickstart
      :link-type: ref
      :class-header: card-header-gray

      Quickstart
      ^^^
      ➡ Installation and basic usage

   .. grid-item-card::
      :link: configuration
      :link-type: ref
      :class-header: card-header-gray

      Configuration
      ^^^
      ➡ Detailed information about all configuration options and examples

   .. grid-item-card::
      :link: contribute
      :link-type: ref
      :class-header: card-header-gray

      Contribute
      ^^^
      ➡ Help improve Sphinx Favicon


.. toctree::
   :hidden:
   :maxdepth: 2

   quickstart
   configuration
   contribute
