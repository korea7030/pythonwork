# -*- coding: utf-8 -*-
from django import forms
from datetimewidget.widgets import DateWidget

from .models import BookInfo, BookCategory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button
from crispy_forms.bootstrap import FormActions


class DateInput(forms.DateInput):
	''' date input class'''

	input_type='date'

class TimeInput(forms.TimeInput):
	''' time input class'''
	input_type='time'

class SubmittedBook(forms.Form):
	# choice field 설정(tuple)
	BOOK_FORMAT_CHOICES = (('', '------'),('Book', 'Book'),('eBook', 'eBook'))
	CATEGORY_BLANK_CHOICES = (('', '------'),)
	BOOK_READYN_CHOICES = (('', '-----'), ('Read', 'Read'), ('Reading', 'Reading'))

	dateTimeOptions = {
		'format' : 'yyyy-mm-dd',
		'autoclose' : True,
	}
	def __init__(self, *args, **kwargs):
		super(SubmittedBook, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method='POST'
		self.helper.form_id='book_form'
		# self.helper.label_class = 'col-lg-2'
		# self.helper.field_class = 'col-lg-8'
		self.helper.form_action='book:index'
		self.helper.layout = Layout(
			Div(
				Div('book_sequence', 'book_title', 'book_subtitle', css_class='col-md-6'),
				Div('author', 'translator', 'publisher', 'publisher_date', css_class='col-md-6')
			),
			Div(
				Div('read_status', 'borrowed_yn',css_class="col-md-6"),
				Div('book_format', 'pages', 'rating', 'category_nm', css_class='col-md-6'),
				Div('start_date', 'end_date', 'book_essay_url', 'poster_url', 'docfile',  css_class='col-md-6')
			),
			Div(Submit('save', '저장'), css_class='row')

		)
	# class Meta:
		# model = BookInfo
		# fields = ('book_sequence', 'book_title', 'book_subtitle', 'author', 'translator', 'publisher', 'publisher_date', 'book_format', 'pages', 'rating', 'category_id', 'start_date', 'end_date')
		#
	book_sequence = forms.CharField(required = True, label="책순번(B1,B2.. 형식으로 입력)")
	book_title = forms.CharField(required = True, label="제목")
	book_subtitle = forms.CharField(required = False, label="부제목")
	author = forms.CharField(required = False, label="저자")
	translator = forms.CharField(required = False, label="번역")
	publisher = forms.CharField(required=False, label="출판사")
	publisher_date = forms.DateField(required=False, label="출판일자", widget=DateInput())
	book_format = forms.ChoiceField(required = True, label="책형태" , choices = BOOK_FORMAT_CHOICES)
	pages = forms.DecimalField(required = True, label='페이지수')
	rating = forms.DecimalField(required = True, label='별점')
	book_essay_url = forms.CharField(widget = forms.HiddenInput(), required=False)
	poster_url = forms.CharField(widget= forms.HiddenInput(), required=False)
	read_status = forms.ChoiceField(required = True, label="읽은상태", choices = BOOK_READYN_CHOICES)
	borrowed_yn = forms.CharField(required=True, label="빌린여부")
	docfile = forms.FileField(required = False, label="파일 업로드")

	## book_category 테이블에서 조회
	# category_id = forms.ChoiceField(label="책종류", required=True, choices = CATEGORY_BLANK_CHOICES + tuple(BookCategory.objects.values('category_id', 'category_div2').values_list('category_id', 'category_div2')))
	category_nm = forms.CharField(required=True,label="책종류")

	start_date = forms.DateField(required=True, label="시작일자", widget=DateInput())
	end_date = forms.DateField(required=True, label="끝일자", widget=DateInput())


class BookHistForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(BookHistForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method='POST'
		self.helper.form_id='book_hist_form'
		self.helper.form_action='book:book_hist_create'
		self.helper.layout = Layout(
			Div(
				Div('book_sequence', 'read_date', 'start_read_time', 'end_read_time', css_class='col-md-6'),
				Div('read_place', 'not_read_reason', 'start_page_num', 'end_page_num', css_class='col-md-6')
			),
			Div(Submit('save', '저장'), css_class='inline-block')

		)

	book_sequence = forms.CharField(widget=forms.HiddenInput(), required = True)
	read_date = forms.DateField(required = True, label = '읽은 날짜', widget=DateInput())
	start_read_time = forms.TimeField(required = False,  widget=TimeInput(), label= '시작시간')
	end_read_time = forms.TimeField(required = False,  widget=TimeInput(), label = '끝난시간')
	read_place = forms.CharField(required = False, label = '읽은 장소')
	not_read_reason = forms.CharField(required = False, label = '읽지 않은 이유')
	start_page_num = forms.DecimalField(required = False, label = '시작페이지')
	end_page_num = forms.DecimalField(required = False, label = '끝난페이지')

