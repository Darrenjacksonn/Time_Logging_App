from .base import *
import os



DEBUG = False

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] 

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

'''
connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('=')[0] : pair.split('=')[1] for pair in connection_string.split(';') if pair}
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : parameters['dbname'],
        'HOST' : parameters['host'],
        'USER' : parameters['user'],
        'PASSWORD' : parameters['password'],
        'PORT' : '5432',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'django',
        'HOST' : "logarhythm-db.postgres.database.azure.com",
        'USER' : 'dazz_o_matic',
        'PASSWORD' : '1522Chiraq8709!',
        'PORT' : '5432',
    }
}


#cnx = psycopg2.connect(user="dazz_o_matic", password="{your_password}", host="logarhythm-db.postgres.database.azure.com", port=5432, database="postgres")



# Security settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] 
