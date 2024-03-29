AUTHOR = 'lancelotly'
SITENAME = u'Lancelot\xb7Sirius\xb7ly'
SITEURL = 'https://lancelotly.github.io'

#GOOGLE_ANALYTICS='UA-57996371-5'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh-CN'

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

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"

#PLUGIN_PATHS = ['plugins']

DEFAULT_PAGINATION = 5
THEME = 'svbhack'
TAGLINE = """Here I'm searching the fantastic nature of our world."""
USER_LOGO_URL = 'https://en.gravatar.com/userimage/59823780/a88754e1f34e09bac8a82ffd9cb2f504.jpeg'
BACK_TO_TOP = 'https://gitlab.com/lancelotly/blog_resources/raw/master/img/xklzhuanquan_org.gif'
SUMMARY_MAX_LENGTH = 30
