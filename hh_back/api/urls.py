from django.urls import path, re_path

from api.views import *
urlpatterns =[
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_det),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/', vacancies),
    path('vacancies/<int:vacancy_id>/', vacancy_det),
    path('vacancies/top_ten/', top_vacancies),
]