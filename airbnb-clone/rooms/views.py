from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models


class HomeView(ListView):
    """ HomeView Definition """
    model = models.Room
    paginate_by = 10
    ordering = 'created'

    # context_data를 임의로 추가가능
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     context['now'] = now
    #     return context


class RoomDetail(DetailView):
    """ RoomDetail Definition"""
    model = models.Room


def search(request):
    city = request.GET.get('city', 'Anywhere')
    room_types = models.RoomType.objects.all()
    country = request.GET.get('country', 'KR')
    room_type = int(request.GET.get('room_type', 0))

    # 변수를 나열해서 쓰는 것이 아닌, 사용되는 element에 따라 나눠서 변수 선언
    # form에서 입력되는 값
    form = {
        'city': city,
        's_country': country,
        's_room_type': room_type
    }

    # selectbox에서 입력되는 값
    choices = {
        'countries': countries,
        'room_types': room_types,
    }
    return render(
        request,
        'rooms/search.html',
        # **를 붙이면 변수들을 나열하는 것과 같은 기능을 한다.
        {**form, **choices},
    )

