from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, this is my Django project!</h1>")
def new(request):
    return HttpResponse("<h1>This is a new page!</h1>")
def data(request):
    return HttpResponse("<h2>На этой странице мы будем работать с данными</h2>")
def test(request):
    return HttpResponse("<h1>Тестирование</h1>")

