from unicodedata import name
from .views import about, categories, index
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cats/<int:catid>/', categories),
]

