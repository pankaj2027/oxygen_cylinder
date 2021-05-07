from django.contrib import admin
from .models import OxygenCylinder
# Register your models here.


@admin.register(OxygenCylinder)
class OxygenCylinderAdmin(admin.ModelAdmin):
    class Meta:
        list_display = '__all__'

