from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'polls/index.html')


def login(request, username, pwd):
    return HttpResponse('login success')
