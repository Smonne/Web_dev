from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404, JsonResponse
from api.models import *
from django.db import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json  = [company.to_json for company in companies]
        return JsonResponse(companies_json, safe=False)
    if request.method == 'POST':
        print(request.body)
        return JsonResponse({})


def company_det(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'the item doesnt exist'}, status = 400)
    return JsonResponse(company.to_json())


def company_vacancies(request, company_id):
    try:
        company= Company.objects.get(id=company_id)
        vacancies = Vacancy.objects.all()
        vacancies_json = [ v.to_json() for v in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'the item doesnt exist'}, status = 400)
    company_vacancy = [v for v in vacancies_json if v['company']==company]
    return JsonResponse(company_vacancy, safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [ v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_det(request, vacancy_id):
    try:
        vacancy= Vacancy.objects.get(id==vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(vacancy.to_json(), safe=False)

def top_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [ v.to_json for v in vacancies]
    newlist = sorted(vacancies_json, key=lambda d: d['salary'])
    try:
        top_ten= newlist[-1:-10]
    except: 
        top_ten = newlist
    return JsonResponse(top_ten, safe=False)