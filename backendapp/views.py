from django.shortcuts import render
from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer

"""
#from .models import Address
from .models import Person_Historical_Diagnostic
from .serializers import Person_Historical_DiagnosticSerializer
from .models import Organization_Address
from .serializers import Organization_AddressSerializer

from .models import Diagnostic
from .serializers import DiagnosticSerializer

from .models import Family
from .serializers import FamilySerializer

from .models import Person_Organization
from .serializers import Person_OrganizationSerializer

from .models import Person_Phone
from .serializers import Person_PhoneSerializer

from .models import Address_Type
from .serializers import Address_TypeSerializer

from .models import Person_Address
from .serializers import Person_AddressSerializer

#from .models import Clinic
#from .models import Clinic_Staff
"""


# Create your views here.

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

"""
class Person_Historical_DiagnosticView(viewsets.ModelViewSet):
    queryset = Person_Historical_Diagnostic.objects.all()
    serializer_class = Person_Historical_DiagnosticSerializer



class Organization_AddressView(viewsets.ModelViewSet):
    queryset = Organization_Address.objects.all()
    serializer_class = Organization_AddressSerializer

class DiagnosticView(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer


class FamilyView(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer



class Person_OrganizationView(viewsets.ModelViewSet):
    queryset = Person_Organization.objects.all()
    serializer_class = Person_OrganizationSerializer


class Person_PhoneView(viewsets.ModelViewSet):
    queryset = Person_Phone.objects.all()
    serializer_class = Person_PhoneSerializer


class Address_TypeView(viewsets.ModelViewSet):
    queryset = Address_Type.objects.all()
    serializer_class = Address_TypeSerializer



class Person_AddressView(viewsets.ModelViewSet):
    queryset = Person_Address.objects.all()
    serializer_class = Person_AddressSerializer

"""