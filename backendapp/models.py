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

    def __str__(self):
        return self.Person_ID


"""class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Street_Address = models.CharField(max_length=100)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Zip_Code = models.CharField(max_length=100)
    Country = models.CharField(max_length=200)
"""


class Person_Historical_Diagnostic(models.Model):
    Dcode = models.IntegerField()
    Person_ID = models.IntegerField()
    Diagnosed_Date = models.CharField(max_length=100)
    Recovery_Status = models.CharField(max_length=100)

    def __str__(self):
        return self.Dcode


class Organization_Address(models.Model):
    Type = models.CharField(max_length=100)
    organization_id = models.IntegerField()
    Address_ID = models.IntegerField()

    def __str__(self):
        return self.Type


class Diagnostic(models.Model):
    DCode = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.DCode



class Family(models.Model):
    Family_ID = models.AutoField(primary_key=True)
    Family_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Family_ID



class Person_Organization(models.Model):
    organization_id = models.IntegerField()
    Relationship_Type = models.CharField(max_length=100)
    Relationship_Status = models.CharField(max_length=100)
    Person_ID = models.IntegerField()

    def __str__(self):
        return self.organization_id


class Person_Phone(models.Model):
    Phone_Number = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Person_ID = models.IntegerField()

    def __str__(self):
        return self.Phone_Number



# mySQL Database Created models 

class Address_Type(models.Model):
    address_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.address_type_id


class Person_Address(models.Model):
    Address_ID = models.IntegerField()
    E_Mail = models.CharField(max_length=100, help_text='TODO: remove this column in favor of person.email')
    address_type_id = models.IntegerField()
    Person_ID = models.IntegerField()

    def __str__(self):
        return self.Address_ID

"""
class Clinic(models.Model):
    clinicid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)



class Clinic_Staff(models.Model):
    clinicid = models.IntegerField()
    Emp_ID = models.IntegerField()

"""



