from django.db import models
# Create your models here.
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    city = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address' : self.address
        }

class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    salary = models.IntegerField()
    company = models.ForeignKey('Company',on_delete=models.CASCADE, related_name='vacancy')

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company' : self.company
        }