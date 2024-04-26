from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('Person_ID','LName','FName','age','Gender','DOB','Religion','DOD','YearsEducation','Ethnicity','Image','Genogram_Image','Ecomap_Image','email')



