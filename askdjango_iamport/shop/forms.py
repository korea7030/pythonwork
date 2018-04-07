from django import forms
from .models import Order
from .mixins import IamportBaseForm


class PayForm(IamportBaseForm):
    template_name = 'shop/_iamport.html'
    params_names = ['merchant_uid', 'name', 'amount']
    imp_fn_name = 'request_pay'

    class Meta:
        model = Order
        fields = ['imp_uid']
        widgets = {
        'imp_uid': forms.HiddenInput,
        }
