from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Persons', views.PersonView)

"""
router.register('backendapp', views.Person_Historical_Diagnostic)
router.register('backendapp', views.Organization_Address)
router.register('backendapp', views.Diagnostic)
router.register('backendapp', views.Family)
router.register('backendapp', views.Person_Organization)
router.register('backendapp', views.Person_Phone)
router.register('backendapp', views.Address_Type)
router.register('backendapp', views.Person_Address)

"""


urlpatterns = [

    path ('', include(router.urls))

    
]
