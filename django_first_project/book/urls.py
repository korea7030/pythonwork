# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from book import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'), # main page
		url(r'^search/$', views.search, name='search'), # search
		url(r'^book_list/$', views.book_list, name='book_list'), # book_list
		url(r'^get_book/$', views.get_book, name='get_book'), # search
		url(r'^update/$', views.book_update, name='book_update'), # update
		url(r'^book_hist_create/$', views.book_hist_create, name='book_hist_create'), # update
		url(r'^book_dash/$', views.book_dash, name='book_dash'), # dash
	)