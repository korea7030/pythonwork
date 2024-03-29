from django.urls import path
from . import views as room_views

app_name = 'rooms'

urlpatterns = [
    # path('', room_views.all_rooms),
    path('<int:pk>', room_views.RoomDetail.as_view(), name='detail'),
    path('search/', room_views.SearchView.as_view(), name='search')
]
