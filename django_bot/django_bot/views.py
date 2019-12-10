import os
import time
import telebot

from django.views import View
from django.http import HttpResponse

from django_bot.settings import BASE_DIR, DOMAIN

from bot.bot import bot
from bot.bot import *

WEBHOOK_SSL_CERT = os.path.join(BASE_DIR, 'webhook_cert.pem')

class ProcessWebhook(View):
    def post(self, request):
        if 'content-length' in request.headers and \
                        'content-type' in request.headers and \
                        request.headers['content-type'] == 'application/json':
            json_string = request.body.decode("UTF-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return HttpResponse('')
        else:
            return HttpResponse(status=403)
    
    def get(self, request):
        return HttpResponse('Hello')
        

bot.remove_webhook()

bot.set_webhook(url=f'https://{DOMAIN}/webhook/', certificate=open(WEBHOOK_SSL_CERT, 'r'))
