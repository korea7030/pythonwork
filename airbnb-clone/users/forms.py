from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # field이름에 clean_을 붙여서 함수를 만들어야 함

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                print(self.cleaned_data)
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email']

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('password confimation does not match')
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user.username = email
        user.set_password(password)
        user.save()


'''
다음과 같이 UserCreationForm을 활용하면 간단하게 만들 수 있음
class SignUpForm(UserCreationForm):
    username = forms.EmailField(label='Email')
'''