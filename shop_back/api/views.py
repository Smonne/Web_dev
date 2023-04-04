from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
# Create your views here.

def hello(request):
    return HttpResponse('hello first')

def product_list(request):
    return HttpResponse('its produc list')


def product_det(request, id):
    return HttpResponse(f'<h1> product id:{id}</h1>')

def category_list(request):
        return HttpResponse('helloooooo')
