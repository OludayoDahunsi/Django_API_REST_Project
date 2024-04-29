from django.contrib import admin
from .models import Person
from .models import Person_Address
from .models import Person_Organization
from .models import Person_Phone
from .models import Person_Historical_Diagnostic
from .models import Clinic
from .models import Clinic_Staff



# Register your models here.
admin.site.register(Person)
admin.site.register(Person_Address)
admin.site.register(Person_Organization)
admin.site.register(Person_Phone)
admin.site.register(Person_Historical_Diagnostic)
admin.site.register(Clinic)
admin.site.register(Clinic_Staff)
