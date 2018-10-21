from django.db.models.signals import post_save
from django.dispatch import receiver
from polls.models import Question, Choice
import os.path

from django.dispatch import Signal

"""
model's save() method is called.
django.db.models.signals.pre_save | post_save

model's delete() method is called.
django.db.models.signals.pre_delete | post_delete

ManyToManyField on a model is changed.
django.db.models.signals.m2m_changed

Django starts or finishes an HTTP request.
django.core.signals.request_started | request_finished
"""

"""
Signal 로 구현
"""
user_login = Signal(providing_args=["notification", "user"])
print(user_login)
"""
receiver decorator로 구현
"""
@receiver(post_save, sender=Question)
def question_post_save(sender, instance, **kwargs):
    """
    signal, instance, created, update_fields, raw, using 은 기본값으로 전달
    created는 row 생성 여부에 따라 True/False
    대량 저장의 경우 호출안됨..
    """
    # print("question_post_save")
    # print(instance)
    # print(instance.params)


@receiver(post_save, sender=Choice)
def choice_post_save(sender, **kwargs):
    print("choice_post_save")
