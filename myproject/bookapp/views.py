from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
# from .custom_auth.LoginBackend import authenticate
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import check_password

from django.template import RequestContext
# from django.utils.safestring import mark_safe

from django.core import serializers

from django.views import generic
from django.views.generic import FormView

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.forms.models import model_to_dict
from .models import BookInfo, ReadHist, BookCategory, BookSaveInfo
from django.db.models import Q
from django.db.models import Count

from .forms import BookInfoAddForm, UserForm, LoginForm
# from backends.LoginBackend import LoginBackend
import requests
import json
import datetime
import os
import time
import jpype
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import matplotlib.font_manager
import networkx
import operator

from konlpy.tag import Twitter  # 시간이 가장 빠름(windows 기준)
from sklearn.feature_extraction.text import CountVectorizer

SWITCH_MAP = {
    'category' 		: 1,
    'rating' 		: 2,
    'format' 		: 3,
    'borrowed_yn' 	: 4,
}


def index(request):
    if request.method == 'POST':
        form = BookInfoAddForm(request.POST)
        response_data = {}

        cate_id = ''
        if form.is_valid():

            book_format = form.cleaned_data['book_format']
            print(request.POST.get('category'))

            if book_format == 'eBook':
                cate_id = BookCategory.objects.filter(Q(cate_1='e북') & Q(
                    cate_2=request.POST.get('category'))).values()
            else:
                cate_id = BookCategory.objects.filter(~Q(cate_1='e북') & Q(
                    cate_2=request.POST.get('category'))).values()

            print(cate_id)
            new_book = form.save(commit=False)
            new_book.reg_date = datetime.datetime.now()
            new_book.cate_cd = cate_id[0]['cate_id']
            # print(new_book.cate_cd)
            new_book.save()
            response_data['result'] = "저장 완료"
            response_data['book_sequence'] = form.cleaned_data['book_sequence']

            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        form = BookInfoAddForm()

    return render(request, 'bookapp/index.html', {'form': form, 'title': 'Books Store Page'})


def search(request):
    ''' daum api를 활용하여 책 정보 조회'''
    apikey = settings.DAUM_API_KEY
    q = request.GET['q']
    res = requests.get(settings.DAUM_API_URL + apikey + "&q=" + q + "&searchType=title")
# res_dict = json.loads(res.text)
    if res.status_code == 200:
        result_txt = res.text

    return HttpResponse(result_txt)


def book_list(request):
    bookList = ''
    q = ''
    category = ''

    if 'q' in request.GET:
        q = request.GET['q']
        if q != '':

            # format_value = request.GET['format_select']
            category = request.GET['category_select']

            if category != '':
                if SWITCH_MAP[category] == 1:  # 책 카테고리별
                    bookList = BookInfo.objects.order_by(
                        '-start_date').all().select_related("cate_cd").filter(Q(cate_cd__cate_2=q))
                    # print(bookList[0].cate_cd.cate_2)
                elif SWITCH_MAP[category] == 2:  # 별점별
                    bookList = BookInfo.objects.order_by(
                        '-start_date').all().select_related("cate_cd").filter(Q(rating=int(q)))
                elif SWITCH_MAP[category] == 3:  # 책 형태별
                    bookList = BookInfo.objects.order_by(
                        '-start_date').all().select_related("cate_cd").filter(Q(book_format=q))
                elif SWITCH_MAP[category] == 4:  # 빌린여부
                    bookList = BookInfo.objects.order_by(
                        '-start_date').all().select_related("cate_cd").filter(Q(borrowed_yn=q))
        else:
            bookList = BookInfo.objects.order_by('-start_date').all().select_related("cate_cd")

    else:
        bookList = BookInfo.objects.order_by('-start_date').all().select_related("cate_cd")

    page = request.GET.get('page')
    paginator = Paginator(bookList, 10)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'bookapp/book_list.html', {'books': books, 'title': 'Book List Page', 'q': q, 'category_select': category})


def signup(request):
    if request.method == 'POST':
        # print(request.POST)
        form = UserForm(request.POST)
        # print(form.cleaned_data.get('username'))
        if form.is_valid():
            # userObj = form.cleaned_data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # print(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists())
            if not (User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
                # print("!")
                user = User.objects.create_user(**form.cleaned_data)
                # user = authenticate(username = username, password = password)
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('/bookapp/')
                # return redirect('index')
            else:
                return HttpResponse('이미 존재하는 회원')
    else:
        form = UserForm()

    return render(request, 'bookapp/adduser.html', {'form': form})


def signin(request):
    User = get_user_model()
    if request.method == "POST":
        form = LoginForm(request.POST)
        # print(form)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(Q(email=email) & Q(password=password)).values()

            if user != None:
                # print("!!!!")
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('/bookapp/')
            else:
                return HttpResponse('로그인 실패')
    else:
        form = LoginForm()

    return render(request, 'bookapp/login.html', {'form': form})


def signout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    # request.session['user_id'] = ''
    logout(request)
    return redirect('/bookapp/')


def get_book(request):
    seq = request.GET['id'].replace(" ", "")

    book = bookList = BookInfo.objects.get(book_sequence=seq)
    return HttpResponse(serializers.serialize("json", [BookInfo.objects.get(book_sequence=seq)]))


def book_update(request):
    if request.is_ajax():
        try:
            seq = request.POST['book_sequence']

            BookInfo.objects.filter(book_sequence=seq).update(book_title=request.POST['book_title'],
                                                              author=request.POST['author'],
                                                              book_format=request.POST['book_format'],
                                                              read_status=request.POST['read_status'],
                                                              pages=request.POST['pages'],
                                                              rating=request.POST['rating'],
                                                              start_date=request.POST['start_date'],
                                                              end_date=request.POST['end_date'])

        except:
            return HttpResponse('Error')
        return HttpResponse('success')

    else:
        pass


def book_dash(request):

    format_keys = ['key', 'values']
    format_tmp = {key: None for key in format_keys}
    yearmonth_tmp = {key: None for key in format_keys}

    # 책 종류별 Count
    book_group_category = BookInfo.objects.all().select_related('cate_cd').values(
        'cate_cd__cate_2').annotate(total=Count('cate_cd__cate_2')).order_by('-total')

    # 책 format별 Count
    book_group_format = BookInfo.objects.all().values(
        'book_format').annotate(total=Count('book_format')).order_by('-total')
    format_tmp['key'] = 'format_group'
    format_tmp['values'] = book_group_format

    extract_query = "to_char(start_date, 'YYYY-MM')"
    yearmonth_count = list(BookInfo.objects.all().extra(select={'read_year_month': extract_query}).values(
        'read_year_month').annotate(count_items=Count('start_date')).order_by('read_year_month'))

    # print(dir(yearmonth_count))
    print(yearmonth_count[0])
    yearmonth_tmp['key'] = 'yearmonth_group'
    yearmonth_tmp['values'] = yearmonth_count

    # rating별 count
    # book_group_rating = BookInfo.objects.all().values('rating').annotate(total=Count('rating')).order_by('-total')

    # book_group_borrowed = BookInfo.objects.all().values('borrowed_yn').annotate(total=Count('borrowed_yn')).order_by('-total')

    books = BookInfo.objects.order_by(
        '-start_date').values('book_title', 'poster_url').select_related("cate_cd")[0:5]
    # print(books)
    return render(request, 'bookapp/book_dash.html', {'book_group_category': list(book_group_category),  'book_group_format': format_tmp, 'yearmonth_count': yearmonth_tmp,  'books': books, 'title': 'Book DASHBOARD'})


def ajax_analytic_word(request):
    # response_data = {}

    if request.is_ajax():
        cate_2 = request.GET['cate_2']
        essay_info = get_array(BookInfo, "book_essay", cate_2)
        # cloud_data = cate_2
        words, count, tdf = words_count(list(essay_info))

        word_corr = np.corrcoef(tdf.todense(), rowvar=0)  # 상관계수

        # edge 구하기
        edges = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                edges.append((words[i], words[j], word_corr[i, j]))

        edges = sorted(edges, key=operator.itemgetter(2), reverse=True)
        edge_list = [(word1, word2) for word1, word2, weight in edges]
        weight_list = [weight for word1, word2, weight in edges]  # 노드 간의 상관성(edge 거리)

        G = networkx.Graph()
        for word1, word2, weight in edges:
            G.add_edge(word1, word2, weight=weight)

        nodes = G.nodes()
        degrees = G.degree(weight="weight")  # node의 크기
        # edge_weight = list(G.edges_iter(data=True))
        # group = networkx.betweenness_centrality(G)

        nodes_dict = [{"id": n, "value": degrees[n]} for n in nodes]  # id: 노드값, value: 노드의 크기
        node_map = dict(zip(nodes, range(len(nodes))))  # 노드의 출발/도착 매핑
        edges_dict = [{"source": node_map[edges[i][0]], "target":node_map[edges[i][1]], "value":weight_list[i]}
                      for i in range(len(edges))]  # source : 출발노드 , target: 도착노드, value: edge 거리(상관계수)

        cloud_data = [{"text": words, "size": cnt} for words, cnt in zip(words, count)]
    else:
        message = '통신 오류'

    # response_data['result'] = cloud_data
    # print(type(cloud_data))
    return HttpResponse(json.dumps({'cloud_data': cloud_data, 'nodes': nodes_dict, 'links': edges_dict}, default=int), content_type="application/json")


def analytic_word(request):
    message = ''

    start_time = time.time()
    q = BookInfo.objects.all().select_related('cate_cd').values('cate_cd__cate_2').distinct()
    print(q[0])
    print("query time %s seconds" % (time.time() - start_time))

    if q:
        essay_info = get_array(BookInfo, "book_essay", q)
        # print("essay_info time %s seconds"  %(time.time() - start_time))

        if essay_info:
            print("list length : " + str(len(list(essay_info))))
            words, count, tdf = words_count(list(essay_info))
            print("word_count time %s seconds" % (time.time() - start_time))

            word_corr = np.corrcoef(tdf.todense(), rowvar=0)  # 상관계수

            # edge 구하기
            edges = []
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    edges.append((words[i], words[j], word_corr[i, j]))

            edges = sorted(edges, key=operator.itemgetter(2), reverse=True)
            edge_list = [(word1, word2) for word1, word2, weight in edges]
            weight_list = [weight for word1, word2, weight in edges]  # 노드 간의 상관성(edge 거리)

            G = networkx.Graph()
            for word1, word2, weight in edges:
                G.add_edge(word1, word2, weight=weight)

            nodes = G.nodes()
            degrees = G.degree(weight="weight")  # node의 크기
            # edge_weight = list(G.edges_iter(data=True))
            # group = networkx.betweenness_centrality(G)

            nodes_dict = [{"id": n, "value": degrees[n]} for n in nodes]  # id: 노드값, value: 노드의 크기
            node_map = dict(zip(nodes, range(len(nodes))))  # 노드의 출발/도착 매핑
            edges_dict = [{"source": node_map[edges[i][0]], "target":node_map[edges[i][1]], "value":weight_list[i]}
                          for i in range(len(edges))]  # source : 출발노드 , target: 도착노드, value: edge 거리(상관계수)

            # 클라우드 출력을 위한 데이터 생성
            cloud_data = [{"text": words, "size": cnt} for words, cnt in zip(words, count)]
            # cloud_data = q[0]

        else:
            message = '텍스트 분석 결과가 없습니다.'
    else:
        message = '등록된 분류 정보가 없습니다.'

    return render(request, 'bookapp/analytic_word.html', {'title': '사용단어', 'categories': q, 'message': message, 'cloud_data': cloud_data, 'nodes': nodes_dict, 'links': edges_dict})


def get_array(Table, column, cate):
    ''' Django ORM의 QuerySet을 single value list로 변환 '''
    if type(cate) is str:
        rows = Table.objects.all().select_related('cate_cd').filter(Q(cate_cd__cate_2=cate)).values(column)
    else:
        rows = Table.objects.all().select_related('cate_cd').filter(
            Q(cate_cd__cate_2=cate[0]['cate_cd__cate_2'])).values(column)

    return [row[column] for row in rows]


def get_word(doc):
    ''' 단어 길이가 1인 단어 및 필요없는 단어 제거'''
    get_word_time = time.time()

    if jpype.isJVMStarted():
        jpype.attachThreadToJVM()  # jpype 문제 해결을 위한 코드

    tagger = Twitter()
    nouns = tagger.nouns(doc)
    # print("tagger nouns time %s seconds" %(time.time() - get_word_time))
    remove_noun = []
    with open(os.path.join(settings.BASE_DIR, 'remove_noun.txt'), 'r', newline="\r\n", encoding='utf8') as f:
        for line in f.readlines():
            remove_noun.append(line.strip())

    res = []
    for noun in nouns:
        if ((len(noun) > 1) & (noun not in remove_noun)):
            res.append(noun)

    # print("get_word time %s seconds" % (time.time() - get_word_time))
    return res


def words_count(essays):
    ''' 단어에 대한 빈도수 가져오는 함수 '''
    word_start_time = time.time()
    # tagger = Kkma()
    # 한글자 인 단어 빼기
    cv = CountVectorizer(tokenizer=get_word, max_features=65)
    tdf = cv.fit_transform(essays)
    words = cv.get_feature_names()

    count_mat = tdf.sum(axis=0)
    count = np.squeeze(np.asarray(count_mat))
    # print("word_count %s seconds" % (time.time() - word_start_time))
    return words, count, tdf
