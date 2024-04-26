from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


from .models import Person_Address
from .serializers import Person_AddressSerializer

from .models import Person_Organization
from .serializers import Person_OrganizationSerializer

from .models import Person_Phone
from .serializers import Person_PhoneSerializer

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

