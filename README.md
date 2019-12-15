# django_bot
It's a template for creating telegram bots based on django using pyTelegramBotAPI

`cd django_bot`

1. Create local_setting.py
2. Copy code from django_bot/prod_settings.py
3. Change it for you
4. Create virtual environment

`virtualenv venv`

5. Install requirements

`pip install -r requirements.py`

6. Create ssl key and certificate

`sudo apt-get install openssl`

`openssl genrsa -out webhook_pkey.pem 2048`

`openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem`

7. Start development server

`python manage.py runsslserver --certificate webhook_cert.pem --key webhook_pkey.pem 0.0.0.0:5000`
