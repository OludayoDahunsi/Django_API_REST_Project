from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from .models import Organization_Address
from .serializers import Organization_AddressSerializer
from .models import Diagnostic
from .serializers import DiagnosticSerializer


# Create your views here.

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



class Organization_AddressView(viewsets.ModelViewSet):
    queryset = Organization_Address.objects.all()
    serializer_class = Organization_AddressSerializer


class DiagnosticView(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer



"""
from .models import Family
from .serializers import FamilySerializer

from .models import Person_Organization
from .serializers import Person_OrganizationSerializer

from .models import Person_Phone
from .serializers import Person_PhoneSerializer
"""




"""
class FamilyView(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer



class Person_OrganizationView(viewsets.ModelViewSet):
    queryset = Person_Organization.objects.all()
    serializer_class = Person_OrganizationSerializer


class Person_PhoneView(viewsets.ModelViewSet):
    queryset = Person_Phone.objects.all()
    serializer_class = Person_PhoneSerializer

"""