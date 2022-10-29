from mysite.settings import *





# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_Root=BASE_DIR/'static'
MEDIA_Root=BASE_DIR/'media'
STATIC_DEPS=True

COMPRESS_ROOT= STATIC_Root
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
CSRF_COOKIE_SECURE=True
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend'] 

