from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login,

urlpatterns = [
    url(r'^$', views.index, {'template_name': 'polls/login.html'} , name='index'),
    url(r'^test$', views.C_view.as_view(), name='index')
]
