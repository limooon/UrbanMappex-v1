import datetime
from pathlib import Path
import os

#gdal imports librery
if os.name == 'nt':
    VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1__sge-*5$_j%01()qi1&n^f(x)z-8oqmhjxwvpt4@j3k2$)k8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'Registro',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'cartografia',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'SSC.urls'

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

WSGI_APPLICATION = 'SSC.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Utiliza el backend específico para PostGIS
        'NAME': 'gis',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
      
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
   
}
SIMPLE_JWT ={
    'ACCESS_TOKEN_LIFETIME':datetime.timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME':datetime.timedelta(days=7)
}
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/


# Usar el algoritmo de hash Argon2
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Agregar sal a las contraseñas (opcional)
PASSWORD_HASHERS += [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Configurar la duración de la sal (opcional)
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Usar sesiones seguras para el restablecimiento de contraseña (opcional)
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"


LANGUAGE_CODE = 'es-me'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de autenticación
LOGIN_URL = 'login'  # Ruta de inicio de sesión
LOGIN_REDIRECT_URL = 'home'  # Ruta de redirección después del inicio de sesión exitoso
LOGOUT_REDIRECT_URL = 'login'  # Ruta de redirección después del cierre de sesión exitoso

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración para una sesión que dura 30 minutos (1800 segundos)
SESSION_COOKIE_AGE = 1800


