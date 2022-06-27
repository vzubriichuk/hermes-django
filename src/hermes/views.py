from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Главная страница Hermes...xuilo11134345')