# Celery finds the tasks written when django applications start.
from .celery import app as celery_app

__all__ = ['celery_app']