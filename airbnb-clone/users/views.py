from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms


# Create your views here.
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")
    # form을 불러올때 reverse를 사용하면 url을 불러오지 않기 때문에 에러 밣생

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    """
    def get(self, request):
        form = forms.LoginForm(initial={'email': 'abc@naver.com'})
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # 모든 필드를 정리해준 결과값.
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('core:home'))
        return render(request, 'users/login.html', {'form': form})
    """


def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        'first_name': 'Nicoas',
        'last_name': 'Serr',
        'email': 'itn@las.com',
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)