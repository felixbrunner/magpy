# from __future__ import unicode_literals

# site
AUTHOR = "Felix Brunner"
SITENAME = "Felix Brunner"
# SITEURL = "https://felixbrunner.github.io" # in publishconf.py
TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"
RELATIVE_URLS = True

# theme
THEME = "pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = None
BOOTSTRAP_FLUID = False
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "liquid_tags.img",
    "liquid_tags.video",
    "liquid_tags.youtube",
    "liquid_tags.vimeo",
    "liquid_tags.include_code",
    "tipue_search",
    "i18n_subsites",
    "pelican_fontawesome",
]
I18N_TEMPLATES_LANG = "en"
PYGMENTS_STYLE = "native"

# template
BOOTSTRAP_NAVBAR_INVERSE = True
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
MENUITEMS = (
    ("Home", "/index.html"),
    # ("Categories", "/categories.html"),
)

# visuals
BANNER = "assets/images/banner.jpg"
BANNER_ALL_PAGES = True
BANNER_SUBTITLE = "My personal website"
FAVICON = "assets/images/avatar.png"  #'images/favicon.ico'
# SITELOGO = "images/logo.png"  # little logo in top navbar as home button
# SITELOGO_SIZE = "20px"  # ??

# sidebar
HIDE_SIDEBAR = False
SIDEBAR_ON_LEFT = False
DISABLE_SIDEBAR_TITLE_ICONS = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = False
TAGS_URL = "tags.html"
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5
DISPLAY_ARCHIVE_ON_SIDEBAR = False
DISPLAY_AUTHORS_ON_SIDEBAR = False
AVATAR = "assets/images/avatar.png"
ABOUT_ME = "Researcher in Econometrics and Data Scientist"
TAG_CLOUD_MAX_ITEMS = 5

# content
TYPOGRIFY = True
DIRECT_TEMPLATES = ("index", "categories", "authors", "archives", "search")
CUSTOM_CSS = "static/custom.css"
CUSTOM_JS = "static/js/custom.js"
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "static/favicon.ico"},
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/custom.js": {"path": "static/custom.js"},
}

# facebook open graph
USE_OPEN_GRAPH = False
OPEN_GRAPH_FB_APP_ID = ""
# OPEN_GRAPH_IMAGE = 'images/avatar.png'

# twitter
TWITTER_CARDS = False

# github
GITHUB_USER = "felixbrunner"
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = "true"
GITHUB_SHOW_USER_LINK = "true"

# links
SOCIAL = (
    (
        "e-mail",
        "mailto:brunner.felix@gmail.com",
        "envelope",
    ),  # at
    # (
    #     "Github",
    #     "https://github.com/felixbrunner",
    # ),
    (
        "LinkedIn",
        "https://pt.linkedin.com/in/brunnerfelix",
    ),
    (
        "Xing",
        "https://www.xing.com/profile/Felix_Brunner13/cv",
    ),
    # (
    #     "StackOverflow",
    #     "https://stackoverflow.com/users/10365292/rubelrennfix",
    #     "stack-overflow",
    # ),
    # (
    #     '<span class="fa fa-code"></span>   Kaggle',
    #     "https://www.kaggle.com/felixbrunner",
    #     "code",
    # ),
    # ('figshare', '###'),
    # ('overleaf', '###'),
    # ('twitter', '###'),
)  ## social links (Name has to be the name of the corresponding FontAwesome icon.)
LINKS = (
    (
        '<span class="fa fa-address-card"></span>&ensp;CV',
        "assets/files/cv.pdf",
    ),
    (
        '<span class="fa fa-graduation-cap"></span>&ensp;Academic CV',
        "assets/files/academic_cv.pdf",
    ),
)
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = False

# email
# EMAIL = "user@example.com"

# google analytics
# GOOGLE_ANALYTICS = ''
# GOOGLE_ANALYTICS_UNIVERSAL = ''
# GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = ''

# disqus (comment section for articles)
# DISQUS_SITENAME = ''
# DISQUS_ID_PREFIX_SLUG = False
# DISQUS_NO_ID = False
# DISQUS_DISPLAY_COUNTS = True

# addthis
# ADDTHIS_PROFILE = 'ra-520d4af6518bf3c7'

## piwik
# PIWIK_URL = ''
# PIWIK_SSL_URL = ''
# PIWIK_SITE_ID = ''

# content license
# CC_LICENSE = "CC-BY-NC-SA" # use alternative below
CC_LICENSE_DERIVATIVES = "ShareAlike"  # "yes","no"
CC_LICENSE_COMMERCIAL = "no"  # "yes"
CC_ATTR_MARKUP = True

# pelican output
PATH = "content"
USE_FOLDER_AS_CATEGORY = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]  # ,'.jpg','.jpeg','.png','.ico','.pdf']
OUTPUT_PATH = "felixbrunner.github.io"
DEFAULT_ORPHANS = 1
DEFAULT_PAGINATION = 10
STATIC_PATHS = [
    "assets",
    "static",
    # "images",
    # "files",
]
# markown
# MARKDOWN = {
#  'extension_configs': {
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.headerid': {},
#  },
#  'output_format': 'html5',
# }

# articles
SHOW_ARTICLE_CATEGORY = True
SHOW_ARTICLE_AUTHOR = False
SHOW_DATE_MODIFIED = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
ARTICLE_EXCLUDES = ["extra"]

# feed
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# structure
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
CATEGORIES_URL = "categories.html"
CATEGORIES_SAVE_AS = "categories.html"


"""
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
"""
