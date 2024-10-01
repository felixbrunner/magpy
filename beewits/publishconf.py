"""This file is used as the configuration file when publishing.
It will import all settings in pelicanconf.py, then modify or extend them.

This file is only used if you use `make publish` or
explicitly specify it as your config file.
"""
from beewits.pelicanconf import *
# import os
# import sys
# from __future__ import unicode_literals

# sys.path.append(os.curdir)

# URL SETTINGS
SITEURL = "https://felixbrunner.github.io/"
RELATIVE_URLS = False

# FEED_ALL_ATOM = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = 'felixbrunner' ??
# GOOGLE_ANALYTICS = 'G-2Y1PCGBZSE'
ANALYTICS = """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-2Y1PCGBZSE"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-2Y1PCGBZSE');
    </script>
"""

ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

SEARCH_URL = "/search"
