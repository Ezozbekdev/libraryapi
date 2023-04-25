from django.contrib import admin
from .models import Book, LibraryModel


admin.site.register(Book)
admin.site.register(LibraryModel)
