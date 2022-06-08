from pathlib import Path

from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definitions

INSTALLED_APPS = [
    # Default Django apps.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third party apps.
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "bootstrap4",
    "debug_toolbar",
    # Local apps
    "learning_logs",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL", default="postgres://postgres@db/postgres"
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa:#E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa:#E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa:#E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa:#E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# My settings
AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_URL = "login"

# django-allauth config
SITE_ID = 1

# Heroku settings
"""
import os  # noqa: F401, F811
import django_heroku
django_heroku.settings(locals())
"""

# django-debug-toolbar
import socket

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# Use the following in Docker only:
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
# Use locally:
# INTERNAL_IPS = ["127.0.0.1"]
