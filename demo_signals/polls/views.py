from django.http import HttpResponse
from django.contrib.auth.views import login as auth_login
from polls import signals
from django.shortcuts import render
from django.views.generic import TemplateView
# from polls.signals import my_signal

# Create your views here.
def index(request, **kwargs):

    if request.method == "POST":
        response = auth_login(request, **kwargs)
        if request.user.is_authenticated():
            print("!!!")
            signals.user_login.send(sender=None, notification="login", user=request.user)

        return response

    return render(request, 'polls/login.html')
    # signals.question_post_save.send(sender=None, name='arg', greeting='hello world')
    # return HttpResponse('aaaa')


class A_view(TemplateView):
    def get(self, request, **kwargs):
        print('get 호출')

    def post(self, request, **kwargs):
        return 'a'


class B_view(TemplateView):
    def get(self, request, **kwargs):
        print('get 호출')

    def post(self, request, **kwargs):
        return 'b'

class C_view(TemplateView):
    template_name = 'polls/login.html'

    def post(self, request, **kwargs):
        a_result = A_view.as_view()(request)
        b_result = B_view.as_view()(request)

        print('call c in a : ', a_result)
        print('call c in b : ', b_result)
