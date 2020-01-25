from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def all_rooms(request):
    # page 처리(only python)
    page = request.GET.get("page", 1)
    page = int(page or 1)

    page_size = 5
    limit = page_size * page
    offset = limit - page_size

    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = models.Room.objects.count() / page_size

    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": ceil(page_count),
            "page_range": range(1, ceil(page_count)),
        },
    )
