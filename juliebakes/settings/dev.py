from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm)+eo%qci9vvwd7-9i4(w3%5%cky-n-)ukuocdy8sz#nh#k+f0'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
