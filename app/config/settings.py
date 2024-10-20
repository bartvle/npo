"""
Django settings for npo project.
"""


import os
from pathlib import Path

from .deploy import DEBUG, SECRET_KEY, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DATABASES, GOOGLE_ANALYTICS_GTAG_PROPERTY_ID


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'wagtail.contrib.forms',
    # 'wagtail.contrib.redirects',
    # 'wagtail.embeds',
    # 'wagtail.sites',
    # 'wagtail.users',
    # 'wagtail.snippets',
    # 'wagtail.documents',
    # 'wagtail.images',
    # 'wagtail.search',
    # 'wagtail.admin',
    # 'wagtail',  
    # 'modelcluster',
    # 'taggit',

    'analytical',

    ## Own content
    'news',
    'activities',
    'newsletter',
    'magazine',
    'amphi',
    'register',
    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

DATABASE_ROUTERS = ['config.routers.DatabaseRouter']


# Password validation

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


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # Stores the file names it handles by appending the MD5 hash of the file’s
    # content to the filename.
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}


# Internationalization

LANGUAGE_CODE = 'nl-BE'

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = False

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'frontend', 'locale')]


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Other

LOGIN_URL = '/admin/login/'

FILE_UPLOAD_PERMISSIONS = 0o644


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# WAGTAIL_SITE_NAME = 'Natuurpunt Oosterzele'
# WAGTAILADMIN_BASE_URL = 'https://www.natuurpuntoosterzele.be'