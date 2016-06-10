from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Welcome to Neutri App For your healthy living')


def home(request):
    return HttpResponse('You are home of healthy living')