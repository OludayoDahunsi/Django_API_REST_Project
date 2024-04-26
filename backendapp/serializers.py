from rest_framework import serializers
from .models import Person
from .models import Organization_Address
from .models import Diagnostic



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','Person_ID','LName','FName','Age','Gender','DOB','Religion','DOD Date','YearsEducation','Ethnicity','Image','Genogram_Image','Ecomp_Image','Email')



