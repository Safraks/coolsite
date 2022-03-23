import re
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Main page")

def categories(request, catid):
    return HttpResponse(f"<h1>Articles by categories<h1>{catid}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
