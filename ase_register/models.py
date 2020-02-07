from django.db import models

# Create your models here.
class Ase(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=20)
    mobile = models.IntegerField(20)
    dateoj = models.DateField()
