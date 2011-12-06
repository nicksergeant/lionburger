import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nick Sergeant', 'nick@lionburger.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'lionburger'
DATABASE_USER = 'lionburgerusr'
DATABASE_PASSWORD = '4mj5v5FvgG7U9CFwBGGd'
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media').replace('\\','/')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '2epx&(otawvi3p$4qo2j0iwb!-1-xraovxc&f75e0fv6_4%@&!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'lionburger.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'compressor',
)

# django-css
COMPRESS_OUTPUT_DIR = "cache"
COMPRESS_JS_FILTERS = []
COMPILER_FORMATS = {
    '.less': {
        'binary_path':'lessc',
        'arguments': '*.less *.css'
    },
}

from local_settings import *
