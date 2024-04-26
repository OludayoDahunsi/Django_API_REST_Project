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


class Person_Address(models.Model):
    Address_ID = models.CharField(max_length=100)
    E_Mail = models.CharField(max_length=100, help_text='TODO: remove this column in favor of person.email')
    address_type_id = models.CharField(max_length=100)
    Person_ID = models.CharField(max_length=100)


class Person_Organization(models.Model):
    organization_id = models.CharField(max_length=100)
    Relationship_Type = models.CharField(max_length=100)
    Relationship_Status = models.CharField(max_length=100)
    Person_ID = models.CharField(max_length=100)
    


class Person_Phone(models.Model):
    Phone_Number = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Person_ID = models.CharField(max_length=100)

            