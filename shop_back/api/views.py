from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404, JsonResponse
from api.models import Product
# Create your views here.

def hello(request):
    return HttpResponse('hello first')

def product_list(request):
    products = Product.objects.all()
    products_json = [ product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_det(request, product_id):
   
    try:
         product = Product.objects.get(id==product_id)
    except Product.DoesNotExist as e:
         #raise Http404
         return JsonResponse({'error': 'product doesn exist'})
    return JsonResponse(product)

def category_list(request):
        return HttpResponse('helloooooo')
