from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from . import models


def all_rooms(request):
    # page 처리(only python)
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)

    try:
        rooms = paginator.get_page(page)
        return render(request, "rooms/home.html", {"rooms": rooms})
    except EmptyPage:
        return redirect("/")
