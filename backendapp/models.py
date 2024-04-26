from django.db import models

# Create your models here

# MSSQL Database Created models 

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('TF', 'Transgender Female'),
        ('TM', 'Transgender Male'),
        ('O', 'Other'),
    ]

    Person_ID = models.AutoField(primary_key=True)
    LName = models.CharField(max_length=100)
    FName = models.CharField(max_length=100)
    age = models.FloatField(null=True, blank=True)
    Gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    DOB = models.DateField(null=True, blank=True)
    Religion = models.CharField(max_length=100, blank=True)
    DOD = models.DateField(null=True, blank=True)
    YearsEducation = models.CharField(max_length=100, blank=True)
    Ethnicity = models.CharField(max_length=100, blank=True)
    Image = models.CharField(max_length=100, blank=True)
    Genogram_Image = models.CharField(max_length=100, blank=True)
    Ecomap_Image = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, blank=True)



class Organization_Address(models.Model):
    Type = models.CharField(max_length=100)
    organization_id = models.IntegerField()
    Address_ID = models.IntegerField()



class Diagnostic(models.Model):
    DCode = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)



