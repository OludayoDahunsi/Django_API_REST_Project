from django.shortcuts import render
from rest_framework import viewsets

# for Person
from .models import Person
from .serializers import PersonSerializer

# for Person Address
from .models import Person_Address
from .serializers import Person_AddressSerializer
# for Person_Organization
from .models import Person_Organization
from .serializers import Person_OrganizationSerializer

#for Person_Phone
from .models import Person_Phone
from .serializers import Person_PhoneSerializer

from .models import Person_Historical_Diagnostic
from .serializers import Person_Historical_DiagnosticSerializer

from .models import Clinic
from .serializers import ClinicSerializer

from .models import Clinic_Staff
from .serializers import Clinic_StaffSerializer


# Create your views here.

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class Person_AddressView(viewsets.ModelViewSet):
    queryset = Person_Address.objects.all()
    serializer_class = Person_AddressSerializer


class Person_OrganizationView(viewsets.ModelViewSet):
    queryset = Person_Organization.objects.all()
    serializer_class = Person_OrganizationSerializer


class Person_PhoneView(viewsets.ModelViewSet):
    queryset = Person_Phone.objects.all()
    serializer_class = Person_PhoneSerializer



class Person_Historical_DiagnosticView(viewsets.ModelViewSet):
    queryset = Person_Historical_Diagnostic.objects.all()
    serializer_class = Person_Historical_DiagnosticSerializer


class ClinicView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class Clinic_StaffView(viewsets.ModelViewSet):
    queryset = Clinic_Staff.objects.all()
    serializer_class = Clinic_StaffSerializer
