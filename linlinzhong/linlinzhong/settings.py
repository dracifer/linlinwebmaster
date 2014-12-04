"""
Django settings for linlinzhong project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r(^aw8$un&(_%jh$zxmb17aw&4%$@0fzf7p-^y!f66=n==4fvm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'linlinzhong.urls'

WSGI_APPLICATION = 'linlinzhong.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mysql_db': {
        # use 'django.db.backends.mysql' for now as 'mysql.connector.django' does not work for latest django. However the former does not work with python3
        'ENGINE' : 'django.db.backends.mysql', 
        'NAME' : 'linlinzhong_v1',
        'USER' : 'linlinzhong',
        'PASSWORD' : 'linlinzhong web',
        'HOST' : '',
        'PORT' : '',
    }
}

# specify database router --
# 'projects.dbRouter.MySqlDbRouter' - router request to mysql DB
DATABASE_ROUTERS = ['projects.dbRouter.MySqlDbRouter']

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Media root
MEDIA_ROOT = os.path.join(BASE_DIR, 'projects/media_files/')

# Media URL need to set according to the server IP (ifconfig)
MEDIA_URL = 'http://192.168.2.106:8100/projects/media_files/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# specifies list of locations to search by django.template.loaders.filesystem.Loader
TEMPLATE_DIRS = (
    #"/home/dracifer/work/web/django_web_server/linlin_v1/linlinzhong/templates",
    os.path.join(BASE_DIR, 'templates/admin'),
    os.path.join(BASE_DIR, 'linlinzhong/templates/themes'),
    os.path.join(BASE_DIR, 'contact/templates/contact'),
    os.path.join(BASE_DIR, 'about/templates/about'),
)

#TODO: Fix sending email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lzdesignweb@gmail.com'
EMAIL_HOST_PASSWORD = 'linlinzhong web'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
