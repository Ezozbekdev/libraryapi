from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import LibraryViewSet, BookViewSet

router = DefaultRouter()
router.register('library', LibraryViewSet, basename='library')
router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.ObtainAuthToken.as_view(), name='obtainAuth')
]