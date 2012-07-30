# Turn on debugging and restart apache if you ever see an "Internal Server Error" page
DEBUG = True

# Set your local timezone (django will try to figure this out automatically)
TIME_ZONE = 'America/Chicago'

# Setting MEMCACHE_HOSTS to be empty will turn off use of memcached entirely
MEMCACHE_HOSTS = ['127.0.0.1:11211']

# Sometimes you need to do a lot of rendering work but cannot share your storage mount
#REMOTE_RENDERING = True
#RENDERING_HOSTS = ['fastserver01','fastserver02']
#LOG_RENDERING_PERFORMANCE = True
#LOG_CACHE_PERFORMANCE = True

# If you've got more than one backend server they should all be listed here
#CLUSTER_SERVERS = []

# If you're using a relay with consistent hashing, you'll need to configure
# this line the same as CH_SERVER_LIST in carbon.conf under [relay]
CARBONLINK_HOSTS = ["127.0.0.1:7002"]

# Override this if you need to provide documentation specific to your graphite deployment
#DOCUMENTATION_URL = "http://wiki.mycompany.com/graphite"

# Enable email-related features
SMTP_SERVER = "127.0.0.1"

# LDAP / ActiveDirectory authentication setup
#USE_LDAP_AUTH = True
#LDAP_SERVER = "ldap.mycompany.com"
#LDAP_PORT = 389
#LDAP_SEARCH_BASE = "OU=users,DC=mycompany,DC=com"
#LDAP_BASE_USER = "CN=some_readonly_account,DC=mycompany,DC=com"
#LDAP_BASE_PASS = "readonly_account_password"
#LDAP_USER_QUERY = "(username=%s)"  #For Active Directory use "(sAMAccountName=%s)"

# If sqlite won't cut it, configure your real database here (don't forget to run manage.py syncdb!)
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2' # or 'postgres'
DATABASE_NAME = 'graphite'
DATABASE_USER = 'graphite'
DATABASE_PASSWORD = 'graphite'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '5432'

# Fix path

LOG_DIR = '/var/log/graphite/webapp'
CSS_DIR = '/usr/share/python-graphite/static/css/'
GRAPHITE_ROOT = '/usr/'
CONF_DIR = '/etc/graphite/'
STORAGE_DIR = '/var/lib/graphite/'
LISTS_DIR = STORAGE_DIR + 'lists/'
INDEX_FILE = STORAGE_DIR + 'index'
WHITELIST_FILE = LISTS_DIR + 'whitelist'
WHISPER_DIR = STORAGE_DIR + 'whisper/'
RRD_DIR = STORAGE_DIR + 'rrd/'
DATA_DIRS = [WHISPER_DIR, RRD_DIR]

TEMPLATE_DIRS = (
    '/usr/share/pyshared/graphite/templates',
)
