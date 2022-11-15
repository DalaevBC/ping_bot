import time
from datetime import datetime
from django.core.management.base import BaseCommand
from pyrogram import Client
from .config import api_id, api_hash
from inside.models import Task


class Command(BaseCommand):
    help = 'Телеграмм бот'
    app = Client(name='first', api_id=api_id, api_hash=api_hash)

    def check_time(self):
        print('check_time')
        tasks = Task.objects.all()
        for task in tasks:

            if task.username.startswith('https://t.me/'):
                task.username.replace('https://t.me/', '')
                print(task.username)
                task.save()

            time_list = task.time_dates()
            current_hour = datetime.now().hour
            if current_hour in time_list:
                chat = self.app.get_chat(task.username.replace('https://t.me/', ''))
                chat_id = chat.id
                print(chat_id)
                self.app.send_message(chat_id, task.task_name)

    def handle(self, *args, **options):
        self.app.start()
        while True:
            self.check_time()
            time.sleep(3600)





