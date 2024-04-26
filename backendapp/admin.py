from django.contrib import admin
from .models import Person
from .models import Organization_Address
from .models import Diagnostic


# Register your models here.
admin.site.register(Person)
admin.site.register(Organization_Address)
admin.site.register(Diagnostic)
