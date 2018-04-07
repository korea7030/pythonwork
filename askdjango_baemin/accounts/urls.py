from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, name='login', kwargs={'template_name': 'accounts/login_form.html'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': reverse_lazy('root')})
]
