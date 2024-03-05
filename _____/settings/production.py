from .base import *
import os



DEBUG = False

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] 

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : parameters['dbname'],
        'HOST' : parameters['host'],
        'USER' : parameters['user'],
        'PASSWORD' : parameters['password'],
    }
}





# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] 
