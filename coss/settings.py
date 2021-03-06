"""
Django settings for coss project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from __future__ import absolute_import, unicode_literals # noqa
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from decouple import config, Csv
from dj_database_url import parse as db_url
from unipath import Path


PROJECT_DIR = Path(__file__).parent.parent
BASE_DIR = Path(__file__).parent.parent.parent
ROOT_URLCONF = 'coss.urls'
STATIC_ROOT = Path('static').resolve()
STATIC_URL = config('STATIC_URL', default='/static/')
MEDIA_ROOT = Path('media').resolve()

# Application definition
INSTALLED_APPS = [
    'coss.base',
    'coss.users',

    'coss.home',
    'coss.search',
    'coss.opensource_clubs',
    'coss.discourse',
    'coss.activate',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.modeladmin',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-axes
    'axes',
    # django-compressor
    'compressor',
    # django-storages
    'storages',
    # Sentry
    'raven.contrib.django.raven_compat'
]

MIDDLEWARE = [
    # Whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coss.wsgi.application'

# User Model
AUTH_USER_MODEL = 'users.User'

# Authentication Backend
AUTHENTICATION_BACKENDS = ['coss.users.backends.CossBackend']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

# Django compressor
COMPRESS_ENABLED = config('COMPRESS_ENABLED', default=True, cast=bool)
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', default=True, cast=bool)
COMPRESS_CACHE_BACKEND = config('COMPRESS_CACHE_BACKEND', default='default')
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter'
]
COMPRESS_PRECOMPILERS = (
    ('text/scss', 'sass --scss {infile} {outfile}'),
)

#######################
# Environment Variables
#######################

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')
TIME_ZONE = config('TIME_ZONE', default='UTC')
USE_I18N = config('USE_I18N', default=True, cast=bool)
USE_L10N = config('USE_L10N', default=True, cast=bool)
USE_TZ = config('USE_TZ', default=True, cast=bool)

DEBUG = config('DEBUG', default=False, cast=bool)
DEV = config('DEV', default=False, cast=bool)
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
SECRET_KEY = config('SECRET_KEY')
SITE_URL = config('SITE_URL', default="http://localhost")
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())

# Cache
CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND',
                          default='django.core.cache.backends.memcached.MemcachedCache'),
        'LOCATION': config('CACHE_URL', default='127.0.0.1:11211'),
    }
}

# S3 storage
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN',
                              default='{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME))
# Media storage
MEDIA_URL = config('MEDIA_URL', default='https://{0}/'.format(AWS_S3_CUSTOM_DOMAIN))
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Social media
SOCIAL_FB_APP_ID = config('SOCIAL_FB_APP_ID', default='118056745560883')

##########
# Security
##########

# Django-axes
AXES_BEHIND_REVERSE_PROXY = config('AXES_BEHIND_REVERSE_PROXY', default=True, cast=bool)
# Security middleware
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=True, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=31536000, cast=int)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Django-csp
CSP_DEFAULT_SRC = (
    "'self'",
)

CSP_FONT_SRC = (
    "'self'",
)

CSP_IMG_SRC = (
    "'self'",
    'https://*.s3.amazonaws.com',
    '*.gravatar.com',
    '*.google-analytics.com',
    'https://cdn.mozillians.org',
)

CSP_SCRIPT_SRC = (
    "'self'",
    'https://*.google-analytics.com',
    'https://*.googletagmanager.com',
    'https://tagmanager.google.com'
)

CSP_STYLE_SRC = (
    "'self'",
)

CSP_CHILD_SRC = (
    "'self'",
)

# Exclude CMS admin from CSP
# https://github.com/wagtail/wagtail/issues/1288
CSP_EXCLUDE_URL_PREFIXES = ('/cms-admin',)

# mozillians.org API
MOZILLIANS_API_URL = config('MOZILLIANS_API_URL', default='https://mozillians.org/api/v2/')
MOZILLIANS_API_KEY = config('MOZILLIANS_API_KEY', default='')

# Sentry setup
if config('MESOS_CLUSTER', default=False, cast=bool):
    RAVEN_CONFIG = {
        'dsn': config('RAVEN_CONFIG_DSN', default=''),
        'release': config('MARATHON_APP_LABEL_VERSION', default=''),
        'environment': config('MARATHON_APP_LABEL_ENV', default=''),
        'name': config('HOST', default=''),
        'tags': {
            'container': config('HOSTNAME', default=''),
            'mesos_task_id': config('MESOS_TASK_ID', default='')
        }
    }

##################
# Wagtail Settings
##################

WAGTAIL_SITE_NAME = "coss"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = config('BASE_URL', default='http://127.0.0.1:8000')

# users.User settings
WAGTAIL_USER_EDIT_FORM = 'coss.users.forms.CossUserEditForm'
WAGTAIL_USER_CREATION_FORM = 'coss.users.forms.CossUserCreationForm'
WAGTAIL_USER_CUSTOM_FIELD = ['site', 'avatar', 'github']

#####################
# DEV, DEBUG Settings
#####################

if DEV:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_URL = '/media/'

    # Disable template caching
    for backend in TEMPLATES:
        del backend['OPTIONS']['loaders']
        backend['APP_DIRS'] = True
