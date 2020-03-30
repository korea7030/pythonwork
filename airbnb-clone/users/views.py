import os
import requests

from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from . import forms, models


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

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(meil_secret=key)
        user.email_confirmed = True
        user.save()
        # TODO: add success message
    except models.User.DoesNotExist:
        # TODO: add error message
        pass

    return redirect(reverse('core:home'))


def github_login(request):
    client_id = os.environ.get('GH_ID')
    redirect_uri = 'http://127.0.0.1:7000/users/login/github/callback'
    print(redirect_uri)
    return redirect(
        f'https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user'
    )


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        code = request.GET.get('code', None)
        client_id = os.environ.get('GH_ID')
        client_secret = os.environ.get('GH_SECRET')

        if code is not None:
            # get github access-token
            token_request = requests.post(f'https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}',
                headers={'Accept': 'application/json'}
            )
            token_json = token_request.json()
            error = result_json.get('error', None)
            if error is not None:
                raise GithubException()
            else:
                access_token = token_json.get('access_token')
                token_api_request = requests.get('https://api.github.com/user', headers={
                    'Authorization': f'token {access_token}', 
                    'Accept': 'application/json'
                    },
                )
                profile_json = token_api_request.json()
                username = profile_json.get('login', None)

                if username is not None:
                    name = profile_json.get('name')
                    email = profile_json.get('email')
                    bio = profile_json.get('bio')

                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException()                        
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            first_name=name, username=email, bio=bio, email=email,
                            login_method=models.User.LOGIN_GITHUB, email_confirmed=True
                        )
                        user.set_unusable_password()
                        user.save()

                    login(request, user)
                    return redirect(reverse('core:home'))    
                else:
                    raise GithubException()
        else:
            raise GithubException()
    except GithubException:
        # send error message
        return redirect(reverse('users:login'))


def kakao_login(request):
    app_key = os.environ.get('KAKAO_APP_KEY')
    redirect_uri = "http://127.0.0.1:7000/users/login/kakao/callback"
    return redirect(f'https://kauth.kakao.com/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code')


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get('code')
        client_id = os.environ.get('KAKAO_APP_KEY')
        redirect_uri = "http://127.0.0.1:7000/users/login/kakao/callback"
        token_request = requests.post(
            f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}',
            headers={'Content-Type': 'application/json;charset=UTF-8'}
        )
        token_json = token_request.json()
        error = token_json.get('error', None)

        if error is not None:
            raise KakaoException()
        
        access_token = token_json.get('access_token')
        profile_request = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f'Bearer {access_token}'})

        print(profile_request.json())
        profile_json = profile_request.json()
        properties = profile_json.get('kakao_account')
        email = properties.get('email')

        if email is None:
            raise KakaoException()

        nickname = properties.get('profile').get('nickname')
        profile_image = properties.get('profile_image_url')

        try:
            user = models.User.objects.get(email=email)
            if user.login_method != models.User.LOGIN_KAKAO:
                raise KakaoException()
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=models.User.LOGIN_KAKAO,
                email_confirmed=True
            )
            user.set_unusable_password()
            user.save()

            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.avater.save(
                    f'{nickname}-avatar', ContentFile(photo_request.content)
                )

        login(request, user)
        return redirect(reverse('core:home'))

    except KakaoException:
        return redirect(reverse('users:login'))
