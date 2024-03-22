# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Mannvirkjaskra Domain Model'
copyright = '2023 Húsnæðis og Mannvirkjastofnun'
author = 'haukur.ludviksson@hms.is'
master_doc = 'index'

html_theme_options = dict(
    project_name = "Hugtakalíkan Mannvirkjaskrár",
    logo = "hmslogo.png",
    logo_alt = "Wagtail",
    logo_height = 60,
    logo_url = "/",
    logo_width = 120,
    github_url = "https://github.com/hms-is/mannvirkjaskra-domain-model/",
    #header_links = "Top 1|http://example.com/one, Top 2|http://example.com/two",
    footer_links = ",".join([
        "About Us|https://hms.is/husnaedis-og-mannvirkjastofnun",
        "Contact|https://hms.is/starfsfolk-hms",
        "Legal|https://hms.is/",
    ]),
)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

#html_theme = 'sphinx_rtd_theme'

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme' 

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

todo_include_todos = True

rst_prolog = """
.. |br| raw:: html

   <br />
"""
