"""
Django settings for portfolio project.

Optimized for PythonAnywhere (SQLite + WhiteNoise + Static Images).
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

# Cargar variables de entorno
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# SEGURIDAD
# ==============================================================================

# IMPORTANTE: Configurar SECRET_KEY en las variables de entorno de DigitalOcean
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dev-key')

# DEBUG debe ser False en producción
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS: Permitir dominios de DigitalOcean y localhost
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
    '.ondigitalocean.app',  # Soporta subdominios de App Platform
    os.getenv('CUSTOM_DOMAIN', '*') # Opcional: tu dominio personalizado
]

# CSRF: Necesario para que el cambio de idioma funcione tras el despliegue
CSRF_TRUSTED_ORIGINS = [
    'https://*.ondigitalocean.app',
    'https://' + os.getenv('CUSTOM_DOMAIN', 'localhost')
]


# ==============================================================================
# APLICACIONES
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Mis Apps
    'projects',
    'skills',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# ==============================================================================
# BASE DE DATOS (MySQL para Producción / SQLite para Local)
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Si existe DATABASE_URL (en DigitalOcean), sobreescribimos la conexión
if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )


# ==============================================================================
# PASSWORD & I18N
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Español')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# ==============================================================================
# ESTÁTICOS
# ==============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

