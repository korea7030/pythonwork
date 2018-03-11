from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum), # url은 무조건 문자열 타입임
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^getname/$', views.post_list1),
    url(r'^post2/$', views.post_list2),
    url(r'^excel/$', views.excel_download),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum), # url은 무조건 문자열 타입임
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum), # url은 무조건 문자열 타입임
]
