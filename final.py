AUTHOR = 'lancelotly'
SITENAME = u'Lancelot\xb7Sirius\xb7ly'
SITEURL = 'https://lancelotly.github.io'

GOOGLE_ANALYTICS='UA-57996371-5'
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

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

#PLUGIN_PATHS = ['plugins']
#PLUGINS = [u'pelican_comment_system']

DEFAULT_PAGINATION = 9
THEME = 'svbhack'
TAGLINE = """Here I'm searching the fantastic nature of our world.""
