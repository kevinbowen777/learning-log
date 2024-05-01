"""Sphinx configuration."""

project = "learning-log"
author = "Kevin Bowen"
copyright = f"2024, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "learning-log"
extensions = [
    "sphinx.ext.duration",
]
