import re
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Women

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница', 'posts': posts,})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    return HttpResponse(f"<h1>Articles by categories<h1>{catid}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


