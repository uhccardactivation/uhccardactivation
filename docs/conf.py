# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'My HTML Website'
author = 'Your Name'
copyright = '2025, Your Name'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx_rtd_theme']  # Enables the Read the Docs theme

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# List of patterns to exclude when looking for source files.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Use the Read the Docs theme

# Include static files
html_static_path = ['_static']

# Path to include custom HTML files
html_extra_path = ['../']  # Ensures your custom HTML files are included
