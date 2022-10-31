from mysite.settings import *

SECRET_KEY = 'django-insecure-w3er8%fui$5$6b7gy+i!@bev=za9t!3d5ovv@3(91y7(^^h9)9'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = True

ALLOWED_HOSTS = ['mohifk.com','www.mohifk.com','127.0.0.1']

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mohifkco_bloger',
        'USER': 'mohifkco_mohi',
        'PASSWORD': 'p,In3gOc4&K2',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



STATIC_Root=BASE_DIR/'static'
MEDIA_Root=BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

COMPRESS_ROOT= STATIC_Root

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend'] 

SECURE_BROWSER_XSS_FILTER = True

## X-Frame-Options
X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'


STATIC_DEPS=True

COMPRESS_ROOT= STATIC_Root