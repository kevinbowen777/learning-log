"""Sphinx configuration."""
project = "learning-log"
author = "Kevin Bowen"
copyright = f"2023, {author}"
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # ToC options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
extensions = [
    'sphinx.ext.duration',
    'sphinx_rtd_theme',
]
