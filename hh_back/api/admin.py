from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(Vacancy)
class AdminVacancy(admin.ModelAdmin):
    list_display= ('id', 'name', 'salary')
admin.site.register(Company)
