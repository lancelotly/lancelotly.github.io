AUTHOR = 'lancelotly'
SITENAME = u'Lancelot\xb7Sirius\xb7ly'
SITEURL = 'https://lancelotly.ml'

#GOOGLE_ANALYTICS='UA-57996371-5'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'

SOCIAL = (('tumblr', 'http://lancelotly.tumblr.com'),
          #('github', ''),
          ('weibo', 'http://weibo.com/lancelotly'),
          ('contact', 'mailto:nmqsly@126.com'),
         )
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'

#PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
#DIRECT_TEMPLATES = ('categories', 'blog-index', 'blog')

#DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

ARTICLE_URL = "{date:%Y}/{date:%c}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%c}/index.html"

#PLUGIN_PATHS = ['plugins']
#PLUGINS = [u'pelican_comment_system']

DEFAULT_PAGINATION = 5
THEME = 'svbhack'
TAGLINE = """Here I'm searching the fantastic nature of our world."""
USER_LOGO_URL = 'https://bitly.com/1TZR48Y'
BACK_TO_TOP = 'https://bitly.com/1Jmm93v'
SUMMARY_MAX_LENGTH = 30
