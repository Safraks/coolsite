from unicodedata import name
from .views import categories, index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories)
]

