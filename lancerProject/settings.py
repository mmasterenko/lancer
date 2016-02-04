# -*- coding: utf-8 -*-

"""
Django settings for lancerProject project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1&f0*-y8f-pzw^h==3y=44%3rxp5!49do)kkam@n5ga7^%d&zs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lancerApp'
)

ADMIN_SHORTCUTS = [
    {
        'title': u'Лансер Сервис',
        'shortcuts': [
            {
                'url_name': 'admin:lancerApp_generalinfo_changelist',
                'title': u'Общая информация',
                'url_extra': '1',
                'class': 'home'
            },
            {
                'url_name': 'admin:lancerApp_news_changelist',
                'title': u'Новости',
                'class': 'date'
            },
            {
                'url_name': 'admin:lancerApp_actions_changelist',
                'title': u'Акции',
                'class': 'blog'
            },
            {
                'url_name': 'admin:lancerApp_stuff_changelist',
                'title': u'Наша команда',
                'class': 'user'
            },
        ]
    },
    {
        'title': u'Машины и услуги',
        'shortcuts': [
            {
                'url_name': 'admin:lancerApp_car_changelist',
                'title': u'Модели машин',
                'class': 'plus'
            },
            {
                'url_name': 'admin:lancerApp_service_changelist',
                'title': u'Услуги',
                'class': 'cash'
            },
        ]
    },
    {
        'title': u'Запчасти',
        'shortcuts': [
            {
                'url_name': 'admin:lancerApp_spares_changelist',
                'title': u'Запчасти',
                'class': 'config'
            },
            {
                'url_name': 'admin:lancerApp_techliquids_changelist',
                'title': u'Тех. жидкости',
                'class': 'warning'
            },
        ]
    },
]

ADMIN_SHORTCUTS_SETTINGS = {
    'hide_app_list': True,
    'open_new_window': False,
}

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

ROOT_URLCONF = 'lancerProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'lancerApp.context_processors.general_info'
            ],
        },
    },
]

WSGI_APPLICATION = 'lancerProject.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# # # # # # # # # #
# heroku settings #
# # # # # # # # # #

DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_dir_dev'),
)

# *** import development settings if exists ***

try:
    from settings_dev import *
except ImportError:
    pass


try:
    from settings_sqlite import *
except ImportError:
    pass

