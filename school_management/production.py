"""
Production settings for school_management project.
These settings extend the base settings and configure for production environment.
"""

from .settings import *
import os
import urllib.parse

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['your-app-name.onrender.com', '.render.com', '*']

# Direct database configuration
if os.environ.get('DATABASE_URL'):
    db_url = os.environ.get('DATABASE_URL')
    url_parts = urllib.parse.urlparse(db_url)
    
    # Extract database connection details from URL
    username = url_parts.username
    password = url_parts.password
    hostname = url_parts.hostname
    port = url_parts.port or '5432'
    database = url_parts.path.lstrip('/')
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': database,
            'USER': username,
            'PASSWORD': password,
            'HOST': hostname,
            'PORT': port,
        }
    }

# Add WhiteNoise middleware for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Add WhiteNoise after SecurityMiddleware

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configure HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True