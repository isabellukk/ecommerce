import os
from pathlib import Path
import config


BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# SECRET_KEY = config.SECRET_KEY
#
# STRIPE_PUBLISHABLE_KEY = config.STRIPE_PUBLISHABLE_KEY
#
# STRIPE_SECRET_KEY = config.STRIPE_SECRET_KEY
#
# STRIPE_ENDPOINT_KEY = config.STRIPE_ENDPOINT_KEY

SECRET_KEY = config.SECRET_KEY

STRIPE_PUBLISHABLE_KEY = config.STRIPE_PUBLISHABLE_KEY

STRIPE_SECRET_KEY = config.STRIPE_SECRET_KEY

STRIPE_ENDPOINT_KEY = config.STRIPE_ENDPOINT_KEY

DEBUG = True

ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1']

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'django_countries',
        'store',
        'cart',
        'account',
        'payment',
        'stripe',
        'orders',
        ]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR, 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'store.context_processors.categories',
                    'cart.context_processors.cart',
                    ],
                },
            },
        ]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CART_SESSION_ID = 'cart'

AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
