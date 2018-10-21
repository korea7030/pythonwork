from django.forms.models import model_to_dict


class ModelDiffMixin(object):
    """
    A model mixin that tracks model fields' values and provide some useful api
    to know what fields have been changed.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        # print('initial : ', self.__initial)
        # print('dict : ', self._dict)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        # print('diffs : ', diffs)
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        super(ModelDiffMixin, self).save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        # print(model_to_dict(self, fields=[field.name for field in
        #                                   self._meta.fields]))
        return model_to_dict(self, fields=[field.name for field in
                                           self._meta.fields])


def get_repr(value):
    if callable(value):
        return '%s' & value()

    return value


def serial_model(modelobj):
    opts = modelobj._meta.fields
    modeldict = model_to_dict(modelobj)

    for m in opts:
        if m.is_relation:
            foreignkey = get_repr(getattr(modelobj, m.name, None))
            if foreignkey:
                try:
                    modeldict[m.name] = serial_model(foreignkey)
                except:
                    pass

    return modeldict




def notification_event(action, ticket_main, ticket_reply=None, changed_fields=None):
    try:
        # logger.info('# ---------- START notification_event ---------- #')
        event_list = []
        # override 된 save에서 호출 한 경우
        if action == "save":
            # 답변에서 save한 경우('save', self.ticket, self, changed_fields)
            ticket_id = ticket_main.id
            if ticket_reply:
                if ticket_reply.member_yn == 'Y':  # 멤버 답변
                    # TK0009 발송(멤버 답변)
                    event_list.append('TK0009')
                    diff_status_list = ticket_main.get_field_diff('status_cd')  # 답변 후 진행상태 변경 시
                    if diff_status_list:
                        new_status_cd = diff_status_list[1]

                        if new_status_cd == '20':
                            # TK0005 발송(진행중 티켓)
                            event_list.append('TK0005')
                        elif new_status_cd == '30':
                            # TK0006 발송(대기로 티켓 변경)
                            event_list.append('TK0006')
                        elif new_status_cd == '40':
                            # TK0007 발송(해결로 티켓 변경)
                            event_list.append('TK0007')
                        elif new_status_cd == '99':
                            # TK0008 발송(종료로 티켓 변경)
                            event_list.append('TK0008')

                if ticket_reply.member_yn == 'N':  # 고객 답변
                    # TK0010 발송(고객 답변)
                    event_list.append('TK0010')
                if ticket_reply.reply_yn == 'N':  # 티켓 메모 추가
                    # TK0011 발송(티켓 메모 추가)
                    event_list.append('TK0011')

            # ticket_main에서 save한 경우('save', self, changed_fields)
            else:
                if ticket_main.pk is None or 'id' in changed_fields:  # create
                    # TK0001 발송(새 티켓 생성)
                    event_list.append('TK0001')
                    # event master whghl gotj
                    if ticket_main.sender_customer__grade_cd in ['20', '30']:  # vip & vvip
                        # TK0002 발송(VIP & VVIP에 의한 발송)
                        event_list.append('TK0002')
                    if ticket_main.charge_member is not None or ticket_main.charge_team is not None:  # assign_ticket
                        # TK0003 발송(담당자 배정)
                        event_list.append('TK0003')
                    if ticket_main.status_cd == '20':  # open ticket
                        # TK0005 발송(진행중 티켓)
                        event_list.append('TK0005')
                # 특정 필드만 save 호출한 경우
                else:  # update
                    print(ticket_main)
                    print(ticket_main.id)
                    ticket_id = ticket_main.id
                    if any(x in changed_fields for x in ['charge_team', 'charge_member', 'importance_cd']):
                        charge_team_diff = ticket_main.get_field_diff('charge_team')
                        charge_member_diff = ticket_main.get_field_diff('charge_member')
                        importance_diff = ticket_main.get_field_diff('importance_cd')

                        if charge_team_diff:
                            # TK0003 발송(담당자 배정)
                            event_list.append('TK0003')
                        if charge_member_diff:
                            # TK0003 발송(담당자 배정)
                            event_list.append('TK0003')
                        if importance_diff:
                            # TK0004 발송(중요도 변경)
                            event_list.append('TK0004')

                    if ticket_main.question_text == 'Y':  # 티켓 삭제
                        # TK0012 발송(티켓 삭제)
                        event_list.append('TK0012')



        # queryset으로 "update" 호출한 경우(models.Manager)
        else:
            print("call update")
            # print(request_update)
            print('dsfsdf' , ticket_main.values().get())
            print('dsfsdf' , type(ticket_main))
            # ticket_id = ticket_main.values().get()['id']

            if any(x in changed_fields for x in ['question_text', 'pub_date']):

                if 'charge_team' in changed_fields:
                    # TK0003 발송(담당자 배정)
                    event_list.append('TK0003')
                if 'charge_member' in changed_fields:
                    # TK0003 발송(담당자 배정)
                    event_list.append('TK0003')
                if 'importance_cd' in changed_fields:
                    # TK0004 발송(중요도 변경)
                    event_list.append('TK0004')

                if 'delete_yn' in changed_fields:
                    # TK0004 발송(중요도 변경)
                    event_list.append('TK0012')


        return event_list

    except:
        pass
