# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'agile/code'
copyright = '2022, Agile Scientific'
author = 'Agile Scientific'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# This is required for GitHub pages, and seems neater than putting
# it in the GitHub build-docs Action. Creates .nojekyll and CNAME.
extensions = ['sphinx.ext.githubpages']
html_baseurl = 'https://code.agilescientific.com'  # Must have protocol.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

html_theme_options = {
    "sidebar_hide_name": True,
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'README.rst']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# https://sphinx-themes.org/sample-sites/furo/
html_theme = 'furo'

html_logo = 'static/agile_open_mini_logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

html_css_files = [
    'custom.css',
]

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'static/favicon.ico'
