from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w3er8%fui$5$6b7gy+i!@bev=za9t!3d5ovv@3(91y7(^^h9)9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_Root=BASE_DIR/'static'
MEDIA_Root=BASE_DIR/'media'

# STATIC_Root = '/home/mohifkir/public_html/static'
# MEDIA_Root = '/home/mohifkir/public_html/media'



STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = 'SAMEORIGIN' 
COMPRESS_ROOT= STATIC_Root
CSRF_COOKIE_SECURE=True
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend'] 





# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'mohi.fk@gmail.com'
# EMAIL_HOST_PASSWORD = 'dshfskljdfh' #past the key or password app here
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'default from email'
# DEFAULT_EMAIL_FROM = 'mohi.fk@gmail.com' 