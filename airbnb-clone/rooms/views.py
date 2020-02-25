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
    price = int(request.GET.get('price', 0))
    guests = int(request.GET.get('guests', 0))
    bedrooms = int(request.GET.get('bedrooms', 0))
    beds = int(request.GET.get('beds', 0))
    baths = int(request.GET.get('baths', 0))
    instant = request.GET.get('instant', False)
    super_host = request.GET.get('super_host', False)

    # 여러건의 입력값을 받을 때 사용
    s_amenities = request.GET.getlist('amenities')  
    s_facilities = request.GET.getlist('facilities')

    # 변수를 나열해서 쓰는 것이 아닌, 사용되는 element에 따라 나눠서 변수 선언
    # form에서 입력되는 값
    form = {
        'city': city,
        's_country': country,
        's_room_type': room_type,
        'price': price,
        'guests': guests,
        'bedrooms': bedrooms,
        'beds': beds,
        'baths': baths,
        's_amenities': s_amenities,
        's_facilities': s_facilities,
        'instant': instant,
        'super_host': super_host
    }

    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    # selectbox에서 입력되는 값
    choices = {
        'countries': countries,
        'room_types': room_types,
        'amenities': amenities,
        'facilities': facilities,
    }

    # 초기 filter 값은 빈값으로 두고 입력값에 따라 조건 설정
    filter_args = {}

    if city != 'Anywhere':
        filter_args['city__startswith'] = city
    
    filter_args['country'] = country

    if room_type != 0:
        filter_args['room_type__pk'] = room_type

    if price != 0:
        filter_args['price__lte'] = price

    if guests != 0:
        filter_args['guests__gte'] = guests

    if bedrooms != 0:
        filter_args['bedrooms__gte'] = bedrooms

    if beds != 0:
        filter_args['beds__gte'] = beds

    if baths != 0:
        filter_args['baths__gte'] = baths
    
    # instant, super_host의 경우 on, False 형태로 값이 들어옴
    # 이를 True 체크하기 위해선 bool 사용
    if bool(instant) is True:
        filter_args['instant_book'] = True

    if bool(super_host) is True:
        filter_args['host__superhost'] = True

    if len(s_amenities) > 0:
        for a_id in s_amenities:
            filter_args['amenities__pk'] = int(a_id)
    
    if len(s_facilities) > 0:
        for f_id in s_facilities:
            filter_args['facilities__pk'] = int(f_id)
    
    # 최종 filter값 Queryset에 설정
    rooms = models.Room.objects.filter(**filter_args)
    
    return render(
        request,
        'rooms/search.html',
        # **를 붙이면 변수들을 나열하는 것과 같은 기능을 한다.
        {**form, **choices, 'rooms': rooms},
    )

