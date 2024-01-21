# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Encyclopedia 3.A'
copyright = '2023, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/Encyclopedia-Home",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}



extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/Pharma-Logo.svg"
html_favicon = "_static/Logo/Pharma-Logo.svg"
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        {
            "url": "https://deugz.github.io/jb-physio/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 🎓 Physio",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-BEMN/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 🌲 BEMN",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-Bio-Cel/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 🦠 Bio Cell",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-ATGB/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp ⚠ ATGB",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-Bio-Mol/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp ⚛ Bio Mol",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-Ch-Therapeutique/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp Chimie Thérapeutique",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-QPS/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp QPS",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-Sc-Analytique/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp Sciences Analytique",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/jb-VASM/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp VASM",
            "attributes": {"target": "_blank"},
        },
    ],
    "header_links_before_dropdown": 6,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Home",
            "url": "https://deugz.github.io/Encyclopedia-Home/build/html/index.html",
            "icon": "fa-solid fa-house",
        },
        {
            "name": "Profile",
            "url": "https://deugz.github.io/nb-profile/_build/html/intro.html",
            "icon": "fa-solid fa-user",
        },
        {
            "name": "Blog",
            "url": "https://deugz.github.io/ab-blog/_website/index.html",
            "icon": "fa-solid fa-blog",
        },
        {
            "name": "Tools",
            "url": "https://deugz.github.io/nb-tools/_build/html/intro.html",
            "icon": "fa-solid fa-screwdriver-wrench",
        },
    ],
    

    "logo": {
        "text": " &nbsp Université &nbsp ",
        "image_dark": "_static/Logo/Caducée_lauriers_Couleur.svg",
        "alt_text": " &nbsp Pharmacie &nbsp &nbsp",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/Cube.css", "css/coffee_cup.css", "css/kittons.css", "css/style_book_shell.css", "css/style_flipping_card.css", "css/style_wheel.css", "css/bender.css"]
html_js_files = ["assets/script/kittons.js", "assets/script/script_flipping_card.js", "assets/script/script_wheel.js", "assets/script/scriptvideo.js", "assets/script/slideshow.js"]

    
