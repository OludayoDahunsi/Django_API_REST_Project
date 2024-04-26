from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Persons', views.PersonView)
router.register('Person_Address', views.Person_AddressView)
router.register('Person_Organization', views.Person_OrganizationView)
router.register('Person_Phone', views.Person_PhoneView)



urlpatterns = [

    path ('', include(router.urls))

    
]
