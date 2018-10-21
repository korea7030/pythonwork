from django.db import models
from .tasks import add, mul
from .mixin import ModelDiffMixin, notification_event, serial_model
from celery import chain, chord


class CustomQueryset(models.query.QuerySet):
    # print("sdfsdfsdf")
    def update(self, *args, **kwargs):
        print('self: ', self.values())
        # super().update(*args, **kwargs)
        old_charge_team = ''
        old_charge_member = ''
        old_importance_cd = ''
        old_delete_yn = ''

        old_object = self.values()
        print(old_object)
        changed_fields=list(kwargs.keys())
        print(changed_fields)
        # super().update(*args, **kwargs)
        # super(self.models.query.QuerySet, self).update(*args,**kwargs)
        super(self.model.QuerySet, self).update(*args,**kwargs)

        print('after update self : ', self.values())
        old_data = Question.objects.values()[0]
        print(old_data)
        events = notification_event("update", old_object, changed_fields=changed_fields)


        # print(events) # 이벤트 리스트
        # print(self.query) # 쿼리 조회값

        if events:
            if 'charge_team' in changed_fields:
                old_charge_team = old_object.values().get()['charge_team']
            if 'charge_member' in changed_fields:
                old_charge_member = old_object.values().get()['charge_member']
            if 'importance_cd' in changed_fields:
                old_importance_cd = old_object.values().get()['importance_cd']
            if 'delete_yn' in changed_fields:
                old_delete_yn = old_object.values().get()['delete_yn']

            ## call(integration)


        # r = mul.delay(list(kwargs.keys()), 3, 4)
        # print(kwargs)
        # kwargs를 받아 update된 필드 넘기기(list(kwargs.keys()))
        # print(r.get())


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQueryset(self.model, using=self._db)


class Question(models.Model, ModelDiffMixin):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')


    def save(self, ignore=None, *args, **kwargs):
        print(ignore)
        super(Question, self).save(*args, **kwargs)
        print('dddd' , self.get_field_diff('question_text')[0])
        print('sssss', self.diff)
        print('kwargs', kwargs)
        ticket_id, events = notification_event("save", self, changed_fields=self.changed_fields)
        # print(ticket_id,events)
        # if ticket_id and events:
        #     for event_rcv in settings.EVENT_RECEIVERS:
        #         logger.info('[Call the event to notify] {event_func} {ticket_id} {event_list}'.format(
        #             event_func=event_rcv, ticket_id=ticket_id, event_list=events))
        #         func = import_string(event_rcv)
        #         r = func.delay(ticket_id, events)
        #         logger.info('[Received the event in tasks] {}'.format(r))

    objects = CustomManager()


class ChoiceManager(models.Manager):
    def get_queryset(self):
        return CustomQueryset(self.model, using=self._db)


class Choice(models.Model, ModelDiffMixin):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    objects = ChoiceManager()
