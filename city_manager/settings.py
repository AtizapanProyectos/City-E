import os
from pathlib import Path

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment-based deployment configuration (Railway / local development).
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
SECRET_KEY = os.environ.get('SECRET_KEY', '')
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = 'django-insecure-local-development-only'
    else:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured('Set SECRET_KEY before starting in production.')


def env_list(name):
    return [value.strip() for value in os.environ.get(name, '').split(',') if value.strip()]


ALLOWED_HOSTS = ['localhost', '127.0.0.1'] + env_list('ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = env_list('CSRF_TRUSTED_ORIGINS')
railway_domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN', '').strip()
if railway_domain:
    ALLOWED_HOSTS.append(railway_domain)
    CSRF_TRUSTED_ORIGINS.append(f'https://{railway_domain}')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 3600 if not DEBUG else 0

APP_LOGIN_USER = os.environ.get('APP_LOGIN_USER', '')
APP_LOGIN_PASSWORD = os.environ.get('APP_LOGIN_PASSWORD', '')

# Keep existing local files; DATA_DIR=/data places mutable files on the Railway volume.
DATA_DIR = Path(os.environ.get('DATA_DIR', str(BASE_DIR))).resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)
ESCUCHA_FILE = DATA_DIR / 'escucha_data.json' if os.environ.get('DATA_DIR') else BASE_DIR / 'maps' / 'escucha_data.json'
MEDIA_ROOT = DATA_DIR / 'media'
MEDIA_URL = '/media/'

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'elections', # Tu app de base de datos
    'maps',      # Tu app de visualización
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'city_manager.urls'

# Configuración de Plantillas (Templates)
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
            ],
        },
    },
]

WSGI_APPLICATION = 'city_manager.wsgi.application'

# Configuración de Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATA_DIR / 'db.sqlite3',
    }
}

# Internacionalización
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Almacenamiento optimizado de WhiteNoise con compresión gzip/brotli
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'