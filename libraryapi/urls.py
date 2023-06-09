from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="LibraryAPI's docs",
        default_version='v1',
        description='! ',
        contact=openapi.Contact(email='ezozbekh8@gmail.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('docs-api-sw/', schema_view.with_ui('swagger', ), name='swagger-doc'),
]
