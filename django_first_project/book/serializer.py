# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import BookInfo, BookCategory, BookReadHist

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookInfo
		fields = ('book_sequence','book_title','book_subtitle','author','translator','publisher','publisher_date','book_format','pages','rating','category_id','start_date','end_date',)

class BookCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BookCategory
		fields = ('category_id', 'category_div1', 'category_div2')

class BookReadHistSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookReadHist
		fields = ('book_sequence', 'start_read_time', 'end_read_time', 'read_place', 'not_read_reason', 'start_page_num', 'end_page_num')
