from .models import BookInfo, ReadHist
from rest_framework import serializers

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ('book_sequence', 'book_title', 'book_subtitle', 'author', 'translator', 'publisher', 'publisher_date', 'book_format', 'pages', 'rating', 'category_nm', 'start_date', 'end_date', 'reg_date', 'book_essay_url', 'poster_url', 'read_status', 'borrowed_yn', 'docfile')

class ReadHistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadHist
        fields = '__all__'
