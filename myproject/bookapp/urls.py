from django.conf.urls import patterns, url
from bookapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),  # main page
                       url(r'^search/$', views.search, name='search'),  # search
                       url(r'^book_list/$', views.book_list, name='book_list'),  # book_list
                       url(r'^join/$', views.signup, name='join'),  # 회원가입
                       url(r'^login/$', views.signin, name='login'),  # 로그인
                       url(r'^logout/$', views.signout, name='logout'),  # 로그인
                       url(r'^get_book/$', views.get_book, name='get_book'),  # 상세정보
                       url(r'^update/$', views.book_update, name='book_update'),  # 상세정보_수정
                       url(r'^dash/$', views.book_dash, name='book_dash'),  # 상세정보_수정
                       url(r'^analytic_word/$', views.analytic_word, name='analytic_word'),  # 사용단어 분석
                       url(r'^ajax_analytic_word/$', views.ajax_analytic_word,
                           name='ajax_analytic_word')  # ajax 분석
                       # url(r'^get_book/$', views.get_book, name='get_book'), # search
                       # url(r'^update/$', views.book_update, name='book_update'), # update
                       # url(r'^book_hist_create/$', views.book_hist_create, name='book_hist_create'), # update
                       # url(r'^book_dash/$', views.book_dash, name='book_dash'), # dash
                       )
