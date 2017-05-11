# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse
from django.http import Http404
from django.db import connection
from django.db.models import Count


import requests
import json

from book.models import BookInfo, BookCategory, BookReadHist, ReadHistList
from book.serializer import BookCategorySerializer, BookReadHistSerializer, BookSerializer
from book.forms import SubmittedBook, BookHistForm

DAUM_API_URL = 'https://apis.daum.net/search/book?apikey='
SWITCH_MAP = {
	'category' 		: 1,
	'rating' 		: 2,
	'format' 		: 3,
	'borrowed_yn' 	: 4,
}
# Create your views here.
# @api_view(['GET', 'POST', 'DELETE'])
def index(request):
	''' view index page(저장페이지)
		책정보 조회하거나 입력하여 저장
	'''
	if request.method=='POST' and request.FILES['docfile']:
		form = SubmittedBook(request.POST)
		if form.is_valid():
			myfile = request.FILES['docfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

			task = BookInfo(**form.cleaned_data)
			task.book_essay_url = settings.MEDIA_URL+myfile.name
			task.save()

			messages.success(request, '저장 되었습니다.') # message 설정
			return redirect('book:index')
		else:
			messages.warning(request, '에러')
	else:
		form = SubmittedBook()

	return render(request, 'book/index.html', {'form': form, 'title' : 'Books Store Page'})

def search(request):
	''' daum api를 활용하여 책 정보 조회'''

	apikey = settings.DAUM_API_KEY
	q =  request.GET['q']

	res = requests.get(DAUM_API_URL+apikey+"&q="+q+"&searchType=title")
	# res_dict = json.loads(res.text)
	if res.status_code == 200:
		result_txt = res.text

	return HttpResponse(result_txt)
	# return HttpResponse(res_dict['channel']['item'])
	#

def book_list(request):
	''' 읽은 책 내역 조회'''

	bookList = ''
	q = ''
	category = ''

	if 'q' in request.GET:
		q = request.GET['q']
		category = request.GET['category_select']

		if category != '':
			if SWITCH_MAP[category] == 1:	# category
				bookList = BookInfo.objects.order_by('-reg_date').filter(category_nm = q).values('poster_url', 'book_sequence','book_title','book_subtitle', 'author', 'book_format','pages', 'rating','category_nm', 'start_date', 'end_date', 'book_essay_url', 'read_status', 'borrowed_yn')
			elif SWITCH_MAP[category] == 2: # rating
				bookList = BookInfo.objects.order_by('-reg_date').filter(rating = int(q)).values('poster_url', 'book_sequence','book_title','book_subtitle', 'author', 'book_format','pages', 'rating','category_nm', 'start_date', 'end_date', 'book_essay_url', 'read_status', 'borrowed_yn')
			elif SWITCH_MAP[category] == 3:  # format
				bookList = BookInfo.objects.order_by('-reg_date').filter(book_format = q).values('poster_url', 'book_sequence','book_title','book_subtitle', 'author', 'book_format','pages', 'rating','category_nm', 'start_date', 'end_date', 'book_essay_url', 'read_status', 'borrowed_yn')
			elif SWITCH_MAP[category] == 4:
				bookList = BookInfo.objects.order_by('-reg_date').filter(borrowed_yn = q).values('poster_url', 'book_sequence','book_title','book_subtitle', 'author', 'book_format','pages', 'rating','category_nm', 'start_date', 'end_date', 'book_essay_url', 'read_status', 'borrowed_yn')
		else:
			bookList = BookInfo.objects.order_by('-reg_date').values('poster_url', 'book_sequence','book_title','book_subtitle', 'author', 'book_format','pages', 'rating','category_nm', 'start_date', 'end_date', 'book_essay_url', 'read_status', 'borrowed_yn'  )
	else :
		bookList = BookInfo.objects.order_by('-reg_date').values('poster_url', 'book_sequence','book_title','book_subtitle', 'author', 'book_format','pages', 'rating','category_nm', 'start_date', 'end_date', 'book_essay_url', 'read_status', 'borrowed_yn'  )

	page = request.GET.get('page')
	# print(page)
	paginator = Paginator(bookList, 10)

	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)

	# print(bookList);
	return render(request, 'book/book_list.html', {'books': books, 'title': 'Book List Page', 'q' : q, 'category_select' : category})

def get_book(request):
	seq = request.GET['id'].replace(' ', '')

	book = BookInfo.objects.get(book_sequence = seq)
	return HttpResponse(serializers.serialize("json", [BookInfo.objects.get(book_sequence = seq)]))

def book_update(request):
	if request.is_ajax():
		try:
			seq = request.POST['book_sequence']

			print(request.POST['read_status'])
			BookInfo.objects.filter(book_sequence = seq).update(book_title = request.POST['book_title'],
			author = request.POST['author'],
			book_format = request.POST['book_format'],
			read_status = request.POST['read_status'],
			pages = request.POST['pages'],
			rating = request.POST['rating'],
			start_date = request.POST['start_date'],
			end_date = request.POST['end_date']
			)
		except :
			return HttpResponse('Error')
		return HttpResponse('success')
	else:
		raise Http404
		# print(request.POST['book_sequence'])

def book_hist_create(request):
	book_info = ""; HistList="";hist_list=""
	form = BookHistForm(request.POST or None)
	if request.method == 'POST':

		if form.is_valid():
			book_hist = BookReadHist(**form.cleaned_data)
			book_hist.save()

			messages.success(request, '저장 되었습니다.') # message 설정
			return redirect('book:book_hist_create')
	else:
		HistList = ReadHistList.objects.select_related('book').values('book__book_sequence', 'book__book_title', 'read_date', 'start_read_time', 'end_read_time', 'read_place', 'not_read_reason', 'start_page_num', 'end_page_num') # 이력 조회

		page = request.GET.get('page')

		paginator = Paginator(HistList, 10)

		try:
			hist_list = paginator.page(page)
		except PageNotAnInteger:
			hist_list = paginator.page(1)
		except EmptyPage:
			hist_list = paginator.page(paginator.num_pages)

		# form = BookHistForm()
		book_info = BookInfo.objects.order_by('reg_date').all() # 책 목록

	return render(request, 'book/book_hist.html' , {'form' : form, 'title' : 'Book Hist Store', 'book_info' : book_info, 'hist_list' : hist_list})

def dictfetchall(cursor):
	''' dictionary 형태로 row 전체 출력'''
	columns = [col[0] for col in cursor.description]
	return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
			]


def book_dash(request):
	## 넘길 data 지정
	category_data = {'name' : [], 'data' : []}
	format_data = {'name' : [], 'data' : []}
	rating_data = {'name' : [], 'data' : []}
	borrowed_data = {'name' : [], 'data' : []}

	## groupby 조회
	book_group_category = BookInfo.objects.all().values('category_nm').annotate(total=Count('category_nm')).order_by('-total') # 카테고리별 count
	book_group_format = BookInfo.objects.all().values('book_format').annotate(total=Count('book_format')).order_by('-total') # format별 count
	book_group_rating = BookInfo.objects.all().values('rating').annotate(total=Count('rating')).order_by('-total') # rating별 count
	book_group_borrowed = BookInfo.objects.all().values('borrowed_yn').annotate(total=Count('borrowed_yn')).order_by('-total') # 빌린여부 count


	category_data = get_chart_data('category', category_data, book_group_category)
	format_data = get_chart_data('format', format_data, book_group_format)
	rating_data = get_chart_data('rating', rating_data, book_group_rating)
	borrowed_data = get_chart_data('borrowed', borrowed_data, book_group_borrowed)

	print(borrowed_data)

	return render(request, 'book/book_dash.html', {'category_data' : json.dumps(category_data), 'format_data' : json.dumps(format_data), 'rating_data' : json.dumps(rating_data), 'borrowed_data' : json.dumps(borrowed_data), 'title' : 'BOOK DASHBOARD'})

def get_chart_data(query_string, data, query_object):
	''' data 생성 함수 '''

	if query_string == "category":
		for obj in query_object:
			# print(type(obj))
			data['name'].append(obj['category_nm'].replace(' ', ''))
			data['data'].append(obj['total'])

	elif query_string == "format":
		for obj in query_object:
			data['name'].append(obj['book_format'].replace(' ', ''))
			data['data'].append(obj['total'])
	elif query_string == "rating" :
		for obj in query_object:
			data['name'].append(obj['rating'])
			data['data'].append(obj['total'])
	elif query_string == "borrowed":
		for obj in query_object:
			data['name'].append(obj['borrowed_yn'].replace(' ', ''))
			data['data'].append(obj['total'])

	return data


