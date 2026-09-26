"""Configuration file for learning-log Sphinx documentation builder."""

# -- Project information ----------------------------------------------
project = "learning-log"
author = "Kevin Bowen"
copyright = f"%Y, {author}"
release = "0.3.7"

# -- General configuration --------------------------------------------
extensions = [
    "sphinx.ext.duration",
    "myst_parser",
]
templates_path = ["_templates"]
exclude_patterns = []
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -----------------------------------------
html_title = "learning-log"
html_theme = "furo"
language = "en"

html_static_path = ["_static"]

html_logo = "images/django_24.png"
html_favicon = "images/django_24.png"
html_last_updated_fmt = ""
html_show_sphinx = True
