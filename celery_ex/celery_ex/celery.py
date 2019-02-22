import os
from celery import Celery

# settings environment
os.environ.setdefault('DJANGO_SETTINGS.MODULE', 'celery_ex.settings')

app = Celery('celery_ex')
app.config_from_object('django.conf:settings', namespace='CELERY')
# load task module from all apps in project
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))