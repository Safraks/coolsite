from unicodedata import name
from .views import about, addpage, contact, index, login, show_post, show_category
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', show_post, name='post'),
    path('category/<int:cat_id>', show_category, name='category')
]

