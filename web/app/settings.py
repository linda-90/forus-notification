"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
from kombu import Exchange, Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'megg_yej86ln@xao^+)it4e&ueu#!4tl9p1h%2sjr7ey0)m25f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "app/templates"),
)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'fcm_django',
    'mail_templated',

    'apps.notification_user',
    'apps.sender',
    'apps.email_sender'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'apps.sender.middleware.SenderMiddleWare',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

# Celery settings

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER', '')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', '')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# EMAIL

# CELERY_EMAIL_TASK_CONFIG = {
#     'queue' : 'email',
#     'rate_limit' : '50/m',  # * CELERY_EMAIL_CHUNK_SIZE (default: 10)
# }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True


# i18
LANGUAGE_CODE = 'nl'

USE_I18N = True
LANGUAGES = (
    ('en', _('English')),
    ('nl', _('Niderlands')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATE_FORMAT = "d-m-Y"
USE_L10N = False



FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "[your api key]",
         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": False,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": True,
}
