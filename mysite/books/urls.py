from django.conf.urls import url, patterns
from books import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
