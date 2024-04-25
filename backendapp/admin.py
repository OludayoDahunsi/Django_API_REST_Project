from django.contrib import admin
from .models import address
from .models import Person

# Register your models here.

admin.site.register(address)
admin.site.register(Person)
