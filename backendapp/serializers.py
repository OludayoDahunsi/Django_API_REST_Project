from rest_framework import serializers
from .models import Person
from .models import Person_Address
from .models import Person_Organization
from .models import Person_Phone
from .models import Person_Historical_Diagnostic
from .models import Address
from .models import Diagnostic
from .models import Organization_Address
from .models import Clinic
from .models import Clinic_Staff



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

class Person_Historical_DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Historical_Diagnostic
        fields = ('Dcode','Person_ID','Diagnosed_Date', 'Recovery_Status')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('Address_ID','Street_Address','City', 'State', 'Zip_Code', 'Country')


class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = ('Dcode','Name')


class Organization_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization_Address
        fields = ('Type','organization_id', 'Address_ID')


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('clinicid','Name')


class Clinic_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic_Staff
        fields = ('clinicid','Emp_ID')