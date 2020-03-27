from __future__ import unicode_literals

# Site metadata
AUTHOR = 'Felix Brunner'
SITENAME = 'Personal Website'
SITEURL = 'https://felixbrunner.github.io'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'EN'


# Theme settings
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'readable'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']
'''
TRIED BEFORE:
 - blueidea: too narrow
 - clean-blog: no page
 - flex: clean & minimalistic, icons do not work
 - pelican-bootstrap3: not working
 - zurb-F5-basic: good, basicS
'''
STATIC_PATHS = ['img', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'


# Page content settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = True
MAIN_MENU = True
MENUITEMS = (('Home', '/home.html'),
             ('About me', '/cv.html'),
             )


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

#icon: trophy
