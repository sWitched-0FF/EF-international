#coding: utf-8
import os
LOGIN_REDIRECT_URL = '/'
ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'accounts.User'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOCALHOST = '192.168.100.5'

CONVERSEJS_BOSH_SERVICE_URL = 'https://{0}:5280/http-bind'.format(LOCALHOST)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'jb7=&3eq!-4oj1-d2((eeub7h*x77u-8-^vm6orjo4#(!syxa)'

# Application definition
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3',
    'ckeditor',
    'conversejs',
    'filer',
    'easy_thumbnails',
    'embed_video',
    'mptt',
    'rest_framework',
    'suit_ckeditor',  
    'south',

    'accounts',
    'gallery',
    'main', #site base main content
)

LANGUAGE_CODE = 'ru'
LANGUAGES = (('ru','Russian'),)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'finter.urls'


SUIT_CONFIG = {
    'ADMIN_NAME': 'F-International',
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU_EXCLUDE': ('auth', 'sites'),
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 'auto',
        'width': 'auto',
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

WSGI_APPLICATION = 'finter.wsgi.application'

SOUTH_MIGRATION_MODULES = {
        'easy_thumbnails': 'easy_thumbnails.south_migrations',
    }