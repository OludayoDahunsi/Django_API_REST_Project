from rest_framework import serializers
from .models import Person
from .models import Person_Address
from .models import Person_Organization
from .models import Person_Phone



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('Person_ID','LName','FName','age','Gender','DOB','Religion','DOD','YearsEducation','Ethnicity','Image','Genogram_Image','Ecomap_Image','email')



class Person_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Address
        fields = ('Address_ID','E_Mail','address_type_id','Person_ID')


class Person_OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Organization
        fields = ('organization_id','Relationship_Type','Relationship_Status','Person_ID')


class Person_PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Phone
        fields = ('Phone_Number','Type','Person_ID')