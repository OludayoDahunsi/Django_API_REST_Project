from django.db import models

# Create your models here.

class address(models.Model):
    Address_ID =  models.CharField(max_length=10)
    Street_Address =models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip_Code = models.CharField(max_length=100) 
    Country = models.CharField(max_length=100)