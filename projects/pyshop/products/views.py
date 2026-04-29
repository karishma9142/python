from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse('Hello karishma')


def new(request):
    return HttpResponse('new product page')