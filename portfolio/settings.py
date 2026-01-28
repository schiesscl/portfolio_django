"""
Django settings for portfolio project.

Optimized for PythonAnywhere (SQLite + WhiteNoise + Static Images).
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

# Cargar variables de entorno
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# SEGURIDAD
# ==============================================================================

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dev-key')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']  # PythonAnywhere se encarga de filtrar el dominio real


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
    # WhiteNoise: Sirve archivos estáticos de forma eficiente
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # LocaleMiddleware: Detecta y activa el idioma del usuario
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
# BASE DE DATOS (SQLite)
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

# Idiomas disponibles
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Español')),
]

# Ruta a los archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# ==============================================================================
# ESTÁTICOS (CSS, JS, IMÁGENES LOCALES)
# ==============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Configuración de almacenamiento moderno (Django 4.2+)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        # WhiteNoise comprimido, pero no estricto (evita errores 500 si falta un archivo)
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Proxy para PythonAnywhere (Gratuito) - Útil si necesitas HTTP request salientes en el futuro
if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    proxy_address = "http://proxy.server:3128"
    os.environ['http_proxy'] = proxy_address
    os.environ['https_proxy'] = proxy_address

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
