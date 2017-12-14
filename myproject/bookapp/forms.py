from django import forms
from .models import BookSaveInfo
from functools import partial
from django.conf import settings
from django.contrib.auth.models import User

class BookInfoAddForm(forms.ModelForm):
	class Meta:
		model = BookSaveInfo
		# fields = '__all__'
		fileds = ['book_sequence','book_title','book_subtitle','auithor','publisher','publisher_date','pages','category','cate_cd',
		  'book_format','rating','borrowed_yn','translator','book_essay','read_status','start_date' ,'poster_url','end_date']
		exclude = ['',]
		include = ['category_nm']

	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data
		# book_sequence = cleaned_data['book_sequence']
		# if book_sequence is None:
		# 	raise forms.ValidationError("필수 항목입니다.")
		# exclude = 'cate'

# 회원가입
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data
		# print(self.request)
		# self.fields["username"] = self.request.username
		# self.fields["email"] = self.request.email
		# self.fields["password"] = self.request.password

# 로그인
class LoginForm(forms.ModelForm):
	# pass
	class Meta:
		model = User
		fields = ['email', 'password']

	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data
