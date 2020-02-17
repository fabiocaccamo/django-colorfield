# -*- coding: utf-8 -*-

import django
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-colorfield'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'colorfield',
]

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
]

if django.VERSION < (2, 0):
    MIDDLEWARE_CLASSES = [
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware'
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]
else:
    MIDDLEWARE = [
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]
    },
},]

database_engine = os.environ.get('DATABASE_ENGINE', 'sqlite')
database_config = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

DATABASES = {
    'default': database_config.get(database_engine),
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'colorfield/public/media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'colorfield/public/static/')
STATIC_URL = '/static/'
