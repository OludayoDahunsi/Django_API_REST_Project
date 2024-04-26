from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Person', views.PersonView)
router.register('Organization_Address', views.Organization_Address)
router.register('Diagnostic', views.Diagnostic)


urlpatterns = [

    path ('', include(router.urls))

    
]
