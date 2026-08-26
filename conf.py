# conf.py
project = "Data Science Tutorials"
copyright = "2026, Hunter Lybbert"
author = "Hunter Lybbert"

extensions = [
    "myst_nb",  # Parses MyST markdown & Jupyter Notebooks (.ipynb)
]

# conf.py

exclude_patterns = [
    "_build",
    "README.md",             # Prevents Sphinx from expecting README.md in a toctree
    "**.ipynb_checkpoints",
    "templates",
]

nb_execution_mode = "off"

html_theme = "pydata_sphinx_theme"
html_title = ""

html_static_path = ["_static"]
html_css_files = ["custom.css"]
templates_path = ["_templates"]

# conf.py

html_theme_options = {
    # -------------------------------------------------------------------------
    # 1. NAVBAR SLOTS (Fixes duplicate header links & removes top search bar)
    # -------------------------------------------------------------------------
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],          # Only renders your external_links
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": [],                  # REMOVES the top-right search button
    
    # -------------------------------------------------------------------------
    # 2. TOP NAVIGATION LINKS
    # -------------------------------------------------------------------------
    "navbar_align": "right",
    "external_links": [
        {"name": "Home", "url": "https://hunterlybbert.com/"},
        {"name": "About", "url": "https://hunterlybbert.com/about"},
        {"name": "Projects", "url": "https://hunterlybbert.com/projects"},
        {"name": "Tutorials", "url": "https://tutorials.hunterlybbert.com/"},
        {"name": "Resume", "url": "https://hunterlybbert.com/resume"},
    ],
    
    # Prevents Sphinx from creating top-level "super heading" links from your docs
    "show_nav_level": 0, 

    # Social links
    # "icon_links": [
    #     {
    #         "name": "GitHub",
    #         "url": "https://github.com/hunter-lybbert",
    #         "icon": "fa-brands fa-github",
    #     },
    # ],
}

# -----------------------------------------------------------------------------
# 3. SIDEBAR CONFIGURATION (Keeps search ONLY on the left sidebar)
# -----------------------------------------------------------------------------
html_sidebars = {
    "**": [
        "search-field.html",    # Left sidebar search bar
        "sidebar-nav-bs.html",  # Left notebook tree
    ]
}
