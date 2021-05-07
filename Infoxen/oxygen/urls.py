from django.urls import path, include
from rest_framework import routers

from .views import OxygenCylinderDetail


router = routers.DefaultRouter()
router.register('oxygen',OxygenCylinderDetail, basename='oxygen')

urlpatterns = [
    path('', include(router.urls))
]
