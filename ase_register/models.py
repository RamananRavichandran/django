from django.db import models
from phone_field import PhoneField

# Create your models here.
class Ase(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=20,unique=True)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    dateoj = models.DateField()
