from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Persons', views.PersonView)
router.register('Person_Address', views.Person_AddressView)
router.register('Person_Organization', views.Person_OrganizationView)
router.register('Person_Phone', views.Person_PhoneView)
router.register('Person_Historical_Diagnostic', views.Person_Historical_DiagnosticView)
router.register('Address', views.AddressView)
router.register('Diagnostic', views.DiagnosticView)
router.register('Organization_Address', views.Organization_AddressView)
router.register('Clinic', views.ClinicView)
router.register('Persons', views.Clinic_StaffView)



urlpatterns = [

    path ('', include(router.urls))

    
]

