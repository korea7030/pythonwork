from celery import shared_task

# creates an instance of the task
@shared_task
def hello():
    print('Hello world')