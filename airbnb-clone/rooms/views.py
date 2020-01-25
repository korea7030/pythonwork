from django.utils import timezone
from django.views.generic import ListView
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
