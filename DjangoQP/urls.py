from django.contrib import admin
from django.urls import path
from QPApp.views import search_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('admin/', admin.site.urls),
]
