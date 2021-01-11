from __future__ import unicode_literals

# Site metadata
AUTHOR = 'Felix Brunner'
SITENAME = 'Felix Brunner'
SITEURL = 'https://felixbrunner.github.io'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'


# Theme settings
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = None
BOOTSTRAP_FLUID = False
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
           'liquid_tags.img',
           'liquid_tags.video',
           'liquid_tags.youtube',
           'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'tipue_search',
           'i18n_subsites',
           'pelican_fontawesome'
           ]
I18N_TEMPLATES_LANG = 'en'
PYGMENTS_STYLE = 'native'


# Template settings
BOOTSTRAP_NAVBAR_INVERSE = True
#SITELOGO = 'images/logo.png' #little logo in top navbar
#SITELOGO_SIZE = '10px' ??
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
MAIN_MENU = True
HIDE_SITENAME = False
#MENUITEMS = (('Home', '/home.html'),
#             ('About me', '/cv.html'),
#             )
BANNER = 'images/banner.jpg'
BANNER_ALL_PAGES = True
BANNER_SUBTITLE = 'My personal website'
FAVICON = 'images/avatar.png'#'images/favicon.ico'


# Sidebar settings
HIDE_SIDEBAR = False
SIDEBAR_ON_LEFT = False
DISABLE_SIDEBAR_TITLE_ICONS = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = False
TAGS_URL = 'tags.html'
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5
DISPLAY_ARCHIVE_ON_SIDEBAR = False
DISPLAY_AUTHORS_ON_SIDEBAR = False
ABOUT_ME = 'I look at data'#'I am me'
AVATAR = 'images/avatar.png'
TAG_CLOUD_MAX_ITEMS = 5


# Page content settings
TYPOGRIFY = True
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
CUSTOM_CSS = 'static/custom.css'
CUSTOM_JS = 'static/js/custom.js'
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'static/favicon.ico'},
                       'extra/custom.css': {'path': 'static/custom.css'},
                       'extra/custom.js': {'path': 'static/custom.js'},
                       }


# External services settings
## Facebook open graph
USE_OPEN_GRAPH = False
OPEN_GRAPH_FB_APP_ID = ''
#OPEN_GRAPH_IMAGE = 'images/avatar.png'
## twitter
TWITTER_CARDS = False
## Github
GITHUB_USER = 'felixbrunner'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = 'true'
GITHUB_SHOW_USER_LINK = 'true'
## links
LINKS = (#('Name', 'https://url'),
         )
## social links (Name has to be the name of the corresponding FontAwesome icon.)
SOCIAL = (('Github', 'https://github.com/felixbrunner', 'Github'),
          ('LinkedIn', 'https://pt.linkedin.com/in/brunnerfelix', 'LinkedIn'),
          ('Xing', 'https://www.xing.com/profile/Felix_Brunner13/cv', 'Xing'),
          ('StackOverflow', 'https://stackoverflow.com/users/10365292/rubelrennfix', 'stack-overflow'),
          ('Kaggle', 'https://www.kaggle.com/felixbrunner', 'kaggle'),
          #('figshare', '###'),
          #('overleaf', '###'),
          #('twitter', '###'),
          ('e-mail', 'mailto:brunner.felix@gmail.com', 'envelope'), #at
          ('CV', 'files/cv.pdf', 'wikipedia-w'), #id-card
          ('Academic CV', 'files/academic_cv.pdf', 'wikipedia-w'), #id-card
          )
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = False
## email
#EMAIL = 'user@example.com'

# Analytics & comments settings
## Google Analytics
#GOOGLE_ANALYTICS = ''
#GOOGLE_ANALYTICS_UNIVERSAL = ''
#GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = ''
## disqus
#DISQUS_SITENAME = ''
#DISQUS_ID_PREFIX_SLUG = False
#DISQUS_NO_ID = False
#DISQUS_DISPLAY_COUNTS = True
## addthis
#ADDTHIS_PROFILE = 'ra-520d4af6518bf3c7'
## piwik
#PIWIK_URL = ''
#PIWIK_SSL_URL = ''
#PIWIK_SITE_ID = ''


# Content license settings
#CC_LICENSE = "CC-BY-NC-SA" # use alternative below
CC_LICENSE_DERIVATIVES = "ShareAlike" #"yes","no"
CC_LICENSE_COMMERCIAL = "no" #"yes"
CC_ATTR_MARKUP = True


# Pelican output settings
PATH = 'content'
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']#,'.jpg','.jpeg','.png','.ico','.pdf']
OUTPUT_PATH = 'felixbrunner.github.io'
DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'static', 'files']


#MARKDOWN = {
#  'extension_configs': {
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.headerid': {},
#  },
#  'output_format': 'html5',
#}


# Article settings
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
#ARTICLE_EXCLUDES = ['extra']
#DISPLAY_ARTICLE_INFO_ON_INDEX  = None


# Feed settings
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# name settings
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''


'''
THEME attempts:
 - blueidea: too narrow
 - clean-blog: no page
 - flex: clean & minimalistic, icons do not work
 - pelican-bootstrap3: not working
 - zurb-F5-basic: good, basicS
BOOTSTRAP_THEME attempts:
 - 'readable' # defaults to white with blue
 - 'simplex' # defaults to red
 - 'sandstone' # defaults to light green
 - 'flatly' # defaults to turqoise
'''
