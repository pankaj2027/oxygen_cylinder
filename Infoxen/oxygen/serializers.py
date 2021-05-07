from .models import OxygenCylinder
from rest_framework import serializers

class OxygenCylinderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OxygenCylinder
        fields = ('address','business_name','person_name','contact','verified_status','TimeStamp')
        extra_kwargs = {'TimeStamp':{'read_only':True}}