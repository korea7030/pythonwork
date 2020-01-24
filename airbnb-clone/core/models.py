from django.db import models


class TimeStampedModel(models.Model):

    """ Tiemstamp definition model"""

    created = models.DateTimeField(auto_now_add=True)  # model이 생성된 경우 저장
    updated = models.DateTimeField(auto_now=True)  # model을 저장할때마다 저장

    class Meta:
        abstract = True
