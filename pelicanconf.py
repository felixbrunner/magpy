from __future__ import unicode_literals

# Site metadata
AUTHOR = 'Felix Brunner'
SITENAME = 'Personal Website'
SITEURL = 'https://felixbrunner.github.io'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'EN'


# Theme settings
THEME = 'themes/pelican-bootstrap3' #working now
#BOOTSTRAP_THEME = 'readable' # defaults to white with blue
#BOOTSTRAP_THEME = 'simplex' # defaults to red
#BOOTSTRAP_THEME = 'sandstone' # defaults to light green
#BOOTSTRAP_THEME = 'flatly' # defaults to turqoise
BOOTSTRAP_NAVBAR_INVERSE = True
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'tipue_search',
           'i18n_subsites']
#PLUGINS = ['i18n_subsites']
'''
TRIED BEFORE:
 - blueidea: too narrow
 - clean-blog: no page
 - flex: clean & minimalistic, icons do not work
 - pelican-bootstrap3: not working
 - zurb-F5-basic: good, basicS
'''
STATIC_PATHS = ['images', 'static']
#STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css', 'extra/@.html', 'extra/~.html', 'extra/in.html', '../CNAME']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/@.html': {'path': '@.html'},
    'extra/~.html': {'path': '~.html'},
    'extra/in.html': {'path': 'in.html'},
    '../CNAME': {'path': 'CNAME'}
    }

FAVICON = 'images/favicon.ico'
CUSTOM_CSS = 'static/custom.css'


# Page content settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = True
MAIN_MENU = True
MENUITEMS = (('Home', '/home.html'),
             ('About me', '/cv.html'),
             )
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
HIDE_SIDEBAR = True
BANNER = 'images/banner.jpg'

USE_OPEN_GRAPH = True
OPEN_GRAPH_FB_APP_ID = '202018593182706'
#OPEN_GRAPH_IMAGE = 'images/dandydev.png'
TWITTER_CARDS = True

CC_LICENSE = "CC-BY-NC-SA"


# Pelican output settings
PATH = 'content'
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ['.git']
OUTPUT_PATH = 'felixbrunner.github.io'
DEFAULT_PAGINATION = 10


# Article settings
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
ARTICLE_EXCLUDES = ['extra']

# Feed settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# External Links
LINKS = (
         #('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),
         )

# Social links
SOCIAL = (('Github', 'https://github.com/felixbrunner'),
          ('LinkedIn', 'https://pt.linkedin.com/in/felix-brunner-abbb786a'),
          ('E-Mail', 'mailto: user@example.com'),
          #('You can add links in your config file', '#'),
          #('Another social link', '#'),
          )

EMAIL = 'user@example.com'



##

#MARKDOWN = {
#  'extension_configs': {
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.headerid': {},
#  },
#  'output_format': 'html5',
#}

#DISQUS_SITENAME = 'felixbrunner-flex' ??
#ADDTHIS_PROFILE = 'ra-520d4af6518bf3c7'

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
