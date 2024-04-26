from django.contrib import admin
from .models import address
from .models import Person

# Register your models here.


admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Person_Historical_Diagnostic)
admin.site.register(Organization_Address)
admin.site.register(Diagnostic)
admin.site.register(Family)
admin.site.register(Person_Organization)
admin.site.register(Person_Phone)
admin.site.register(Address_Type)
admin.site.register(Person_Address)
admin.site.register(Clinic)
admin.site.register(Clinic_Staff)


