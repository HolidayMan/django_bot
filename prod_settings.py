import os
from django_bot.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TOKEN = "<your token>"

SECRET_KEY = '<your SECRET_KEY>' # django SECRET_KEY

DOMAIN = 'my_domain'
