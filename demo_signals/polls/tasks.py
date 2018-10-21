from celery import Celery
from celery import shared_task

app = Celery('task', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@shared_task(track_started=True)
def add(dict_obj, x, y):
    print(dict_obj)
    return x + y


@shared_task
def mul(list_obj, x, y):
    print('call : ', list_obj)
    return x * y
