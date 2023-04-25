from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from .models import Book, LibraryModel
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .serializers import BookSerializer, LibrarySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        return Book.objects.all()


class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return LibraryModel.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
