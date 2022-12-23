import os

import environ

root = environ.Path(__file__)
env = environ.Env()
environ.Env.read_env()

SITE_ROOT = root()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.abspath(__file__)

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'knox',
    'corsheaders',
    'thumbnails',
]

LOCAL_APPS = [
    'artists.apps.ArtistsConfig',
    'tracks.apps.TracksConfig',
    'accounts.apps.AccountsConfig',
    'playlists.apps.PlaylistsConfig',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    "default": env.db()
}


ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 4,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ],
    "SERIALIZER_EXTENSIONS": {
        "USE_HASH_IDS": True,
        "HASH_IDS_SOURCE": "config.HASH_IDS",
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

HASHIDS_SALT = env.str("HASHIDS_SALT")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


THUMBNAILS = {
    'METADATA': {
        'BACKEND': 'thumbnails.backends.metadata.DatabaseBackend',
    },
    'STORAGE': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'SIZES': {
        'small': {
            'PROCESSORS': [
                {'PATH': 'thumbnails.processors.resize', 'width': 75, 'height': 75},
                {'PATH': 'thumbnails.processors.crop', 'width': 80, 'height': 80}
            ],
            'POST_PROCESSORS': [
                {
                    'PATH': 'thumbnails.post_processors.optimize',
                    'png_command': 'optipng -force -o7 "%(filename)s"',
                    'jpg_command': 'jpegoptim -f --strip-all "%(filename)s"',
                },
            ],
        },
        'large': {
            'PROCESSORS': [
                {'PATH': 'thumbnails.processors.resize', 'width': 120, 'height': 80},
                {'PATH': 'thumbnails.processors.flip', 'direction': 'horizontal'}
            ],
        },
        'watermarked': {
            'PROCESSORS': [
                {'PATH': 'thumbnails.processors.resize', 'width': 20, 'height': 20},
                # Only supports PNG. File must be of the same size with thumbnail (20 x 20 in this case)
                {'PATH': 'thumbnails.processors.add_watermark', 'watermark_path': 'watermark.png'}
            ],
        }
    }
}
