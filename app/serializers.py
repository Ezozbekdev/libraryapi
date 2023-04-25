from rest_framework import serializers
from .models import Book, LibraryModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryModel
        fields = '__all__'
