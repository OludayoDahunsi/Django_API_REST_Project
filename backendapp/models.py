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



class Person_Historical_Diagnostic(models.Model):
    Dcode = models.CharField(max_length=100)
    Person_ID = models.CharField(max_length=100)
    Diagnosed_Date = models.CharField(max_length=100)
    Recovery_Status = models.CharField(max_length=100)



class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Street_Address = models.CharField(max_length=100)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Zip_Code = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)


class Diagnostic(models.Model):
    Dcode = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)



class Organization_Address(models.Model):
    Type = models.CharField(max_length=100)
    organization_id = models.IntegerField()
    Address_ID = models.IntegerField()




class Clinic(models.Model):
    clinicid = models.AutoField(max_length=100)
    Name = models.CharField(max_length=100)



class Clinic_Staff(models.Model):
    clinicid = models.CharField(max_length=100)
    Emp_ID = models.CharField(max_length=100)



            