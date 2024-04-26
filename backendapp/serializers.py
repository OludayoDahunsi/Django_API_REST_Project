from rest_framework import serializers
from .models import Person
#from .models import Address
from .models import Person_Historical_Diagnostic
from .models import Organization_Address
from .models import Diagnostic
from .models import Family
from .models import Person_Organization
from .models import Person_Phone
from .models import Address_Type
from .models import Person_Address
#from .models import Clinic
#from .models import Clinic_Staff


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        field = ('id','Person_ID','LName','FName','Age','Gender','DOB','Religion','DOD Date','YearsEducation','Ethnicity','Image','Genogram_Image','Ecomp_Image','Email')


""""
class AddressSerializer(serializers.ModelSerializer)
    class Meta:
        model = Address
        field = ('id','Address_ID','Street_Address','City','State','Zip_Code','Country')
"""

class Person_Historical_DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Historical_Diagnostic
        field = ('id','Dcode','Person_ID','Diagnosed_Date','Recovery_Status')


class Organization_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization_Address
        field = ('id', 'id', 'Type', 'organization_id', 'Address_ID')



class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        field = ('id','DCode','Name')

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        field = ('id','Family_ID','Family_Name')


class Person_OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Organization
        field = ('id', 'organization_id', 'Relationship_Type', 'Relationship_Status', 'Person_ID')


class Person_PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Phone
        field = ('id', 'Phone_Number', 'Type', 'Person_ID')



class Address_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address_Type
        field = ('id', 'address_type_id', 'name')


class Person_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Address
        field = ('id', 'Address_ID', 'organization_id', 'E_Mail', 'address_type_id', 'Person_ID')


    
