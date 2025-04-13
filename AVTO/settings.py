import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = ['*', '65.1.108.172', '65.1.108.172,65.1.108.172', 'ec2-65-1-108-172.ap-south-1.compute.amazonaws.com', 'localhost']

BASE_URL = 'http://109.73.207.12:800'

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'django_filters',
    'corsheaders',

    'apps.common',
    'apps.america',
    'apps.korea',
    'apps.dubai',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AVTO.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'AVTO.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ],
}

CSRF_TRUSTED_ORIGINS = [
    "http://109.73.207.12:800", 
    "https://109.73.207.12:800", 
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://109.73.207.12",
    "http://109.73.207.12:800",
    "http://109.73.207.12:3000"
 ]

CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
CORS_ALLOW_HEADERS = [
    'accept', 'accept-encoding', 'authorization', 'content-type', 'dnt',
    'origin', 'user-agent', 'x-csrftoken', 'x-requested-with', 'accept-language'
]

CORS_EXPOSE_HEADERS = ['Content-Length', 'X-CSRFToken', 'Access-Control-Allow-Origin']
CORS_ALLOW_CREDENTIALS = True

JAZZMIN_SETTINGS = {
    "site_title": "Askar Avto",
    "site_header": "Askar Avto",
    "site_brand": "Askar Avto",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Добро пожаловать в администратора Askar Avto",
    "copyright": "Askar Avto © 2023-2025",
    "user_avatar": None,
    "show_sidebar": True,
    "navigation_expanded": True,
    "sidebar_fixed": True,
    "sidebar_collapsible": True,

    "order_with_respect_to": [
        "common",
        "america",
        "dubai",
        "korea",
        "auth",
    ],

    "labels": {
        "common": "Общее",
        "america": "Америка",
        "dubai": "Дубай",
        "korea": "Корея",
        "auth": "Аутентификация и Авторизация",

    },

    "custom_links": {
        "common": [
            {
                "name": "Панель мониторинга",
                "url": "admin:index",
                "icon": "fas fa-tachometer-alt",
            },
        ],
    },

    "icons": {
        "common.CarBrand": "fas fa-industry",
        "common.CarModel": "fas fa-car-side",
        "common.Color": "fas fa-palette",
        "common.BodyType": "fas fa-car",
        "common.Manager": "fas fa-user-tie",
        "common.Interior": "fas fa-couch",
        "common.CarHistory": "fas fa-history",
        "common.CarPhoto": "fas fa-camera-retro",

        "america.America": "fas fa-flag-checkered",
        "america.ComparisonsAmerica": "fas fa-balance-scale",

        "dubai.Dubai": "fas fa-city",
        "dubai.ComparisonsDubai": "fas fa-balance-scale",

        "korea.Korea": "fas fa-car",
        "korea.ComparisonsKorea": "fas fa-balance-scale"
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "related_modal_back": False,
    "hide_apps": [],
    "hide_models": [],
    "changeform_format": "horizontal_tabs",
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
}
