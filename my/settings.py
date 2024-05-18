from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

import logging

logger = logging.getLogger('django')

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xp&yozbvpo^zxbp+_-e#emd^tksi#tigpc#!^%x%qbhiu^08o8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'django_filters',
    'protect',
    'sign',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
    "crispy_forms",
    "crispy_bootstrap5",

]
SITE_ID=1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware' 
]

ROOT_URLCONF = 'my.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'my.wsgi.application'


STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'


ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru' 
EMAIL_PORT = 465 
EMAIL_HOST_USER = os.getenv('HOST_USER') 
EMAIL_HOST_PASSWORD = os.getenv('HOST_PASSWORD')  # пароль от почты
EMAIL_USE_SSL = True 
DEFAULT_FROM_EMAIL = os.getenv ('FROM_EMAIL')

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам) 
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
 
# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

SITE_URL= 'http://127.0.0.1:8000'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{', 
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt':'%d.%m.%Y %H-%M-%S',
        },
        'simple_warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
        },
        'simple_error': {
            'format': '%(asctime)s %(levelname)s %(message)s %(exc_info)s',
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt':'%d.%m.%Y %H-%M-%S',
        },
        'errors': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s %(exc_info)s',
            'datefmt':'%d.%m.%Y %H-%M-%S',
        },
        'email': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt':'%d.%m.%Y %H-%M-%S',
        },
        'security': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt':'%d.%m.%Y %H-%M-%S',
        },

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_warning'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_error'
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logging/general.log',
            'formatter': 'general'
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logging/errors.log',
            'formatter': 'errors'
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logging/security.log',
            'formatter': 'security'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors','mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors','mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors'],
            'propagate': True,
        },
    }
}


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"