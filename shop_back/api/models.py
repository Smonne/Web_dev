from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(default='', max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active= models.BooleanField(default= False)