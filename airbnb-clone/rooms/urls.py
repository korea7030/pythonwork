from django.conf.urls import url
from . import views as room_views

urlpatterns = [
    url(r'', room_views.all_rooms),
]
