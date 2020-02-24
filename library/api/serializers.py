from rest_framework import serializers
from ..models import Book
from ..models import Genre
from ..models import Quote

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['owner', 'title', 'url_address', 'picture', 'Overview', 'download', 'created', 'genre']

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['owner', 'from_writer', 'from_book', 'Overview', 'url_address', 'created']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields=['name']


