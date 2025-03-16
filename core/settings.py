"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent  # Trỏ đến thư mục gốc

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g^ljb7lqkhrj6ew)$%9+*6z-86(!#uedo(0xm5!^rf(#x#@*ieiekmdoj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# COMPRESS_ENABLED = True
# COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']
# COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']

ALLOWED_HOSTS = ['laodong.onrender.com', 'localhost', '127.0.0.1']
SITE_ID = 1
SITE_URL = "https://laodong.onrender.com"
DOMAIN_NAME = "laodong.onrender.com"
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
# Application definition
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'sorl.thumbnail',
    # 'cloudinary',
    'smart_selects',
    'captcha',
    # 'compressor',
    'core',
    'parler',
    'ckeditor',
    'ckeditor_uploader',
    'city',
    'profession',
    'blog',
    'page',
    'work',
    'user'
]

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'page.middleware.ResetDailyPostLimitMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'core.urls'

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
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'qCwvQLnYBGrjVrCRGvuCOmmqzfARDflX',
        'HOST': 'turntable.proxy.rlwy.net',
        'PORT': '43733',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

INSTALLED_APPS += ["cloudinary", "cloudinary_storage"]

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dohcwmo3f",
    "API_KEY": "512554783314115",
    "API_SECRET": "7kyjNhG1z4JDtyhAdVJ37p55AHE",
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

TIME_ZONE = 'Asia/Ho_Chi_Minh'

LANGUAGES = [
    ("en", ("English")),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
USE_I18N = True
USE_L10N = True
USE_TZ = True

PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
    ),
    'default': {
        'fallback': ['en'],
        'hide_untranslated': True,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
#STATIC_URL = 'https://vietnamvisa-m4htahr3pzs8oxbgi8.stackpathdns.com/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     # other finders..
#     'compressor.finders.CompressorFinder',
# )


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 1200,
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = 'https://res.cloudinary.com/dohcwmo3f/image/upload/v1/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# GDAL_LIBRARY_PATH = r'D:\miniconda3\Library\bin\gdal.dll'
# GEOS_LIBRARY_PATH=r'D:\miniconda3\Library\bin\geos_c.dll'

# GDAL_LIBRARY_PATH =  "D:\\Python\\python lib\\Lib\\site-packages\\osgeo\\gdal304.dll"
# GEOS_LIBRARY_PATH =  "D:\\Python\\python lib\\Lib\\site-packages\\osgeo\\geos_c.dll"

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'search.provider': 'nominatim',
    'provider.openstreetmap.max_zoom': 18,
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

FRC_CAPTCHA_SECRET = 'A1FVGM405CP677SUQ6P7IQ8SCV9O91T5M09JLPQ56PL6KR6PM8OANLVQPR'
FRC_CAPTCHA_SITE_KEY = 'FCMTV46MG0CMSLU3'
FRC_CAPTCHA_VERIFICATION_URL = 'https://api.friendlycaptcha.com/api/v1/siteverify'
FRC_CAPTCHA_FAIL_SILENT = False



AUTH_USER_MODEL = 'user.CustomUser'