from django.contrib import admin
from .models import Person
from .models import Person_Address
from .models import Person_Organization
from .models import Person_Phone



# Register your models here.
admin.site.register(Person)
admin.site.register(Person_Address)
admin.site.register(Person_Organization)
admin.site.register(Person_Phone)
