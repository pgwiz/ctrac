import os
'''
Django settings for ctrack project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
'''

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4y=sydmh)kb#lqyanw-x36prbj)(($a)zhpuk(%dym=1njd83-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'www.r-ctr.popox.online',
    'r-ctr.popox.online',
    'www.ctr.popox.online',
    'ctr.popox.online',
    '80.93.187.96',
    '127.0.0.1',
    'localhost',
    '.vercel.app',
    'ctracweb.vercel.app',
    'ctrac-c30fznfnw-pgwizs-projects.vercel.app',
    'ctracweb-pgwizs-projects.vercel.app',
]


LOGIN_URL = 'login'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1209600  # 2 weeks, for example
LOGIN_REDIRECT_URL = 'index'

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'car_tracker_app', 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'  # It's good practice to start with a leading slash
STATICFILES_DIRS = [
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')  # No comma here

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'car_tracker_app',
    'crispy_forms',
    'crispy_bootstrap4',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#AUTH_USER_MODEL = 'car_tracker_app.CustomUser'  # Replace 'car_tracker_app' with the correct app name

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ctrack.urls'

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

WSGI_APPLICATION = 'ctrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
'''
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME' : os.path.join(BASE_DIR, 'db.sqlite3')
         #'NAME': BASE_DIR / 'db.sqlite3',
     }
 }
 '''
#brinpeter6-db-server
#dbos_user
#MC45MzUxNDIyOTAzNzAyODc3
# settings.py



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'avnadmin',
        'PASSWORD': 'AVNS_-OUrX1BfTIjgrk3NjrJ',
        'HOST': 'ctrack-brinpeter6-8d6c.h.aivencloud.com',
        'PORT': '14757',
        'OPTIONS': {
            'sslmode': 'require',
            'sslrootcert': 'ctrack/ca.pem',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


'''
# Proxy settings
USE_X_FORWARDED_HOST = True  # If your proxy server sets the X-Forwarded-Host header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # If your proxy server uses HTTPS

# Configure the proxy for outgoing requests
os.environ['HTTPS_PROXY'] = 'https://192.168.160.11:7071'  # Replace with your proxy details
os.environ['HTTP_PROXY'] = 'http://192.168.160.11:7071'  # If you need a proxy for HTTP as well
'''
