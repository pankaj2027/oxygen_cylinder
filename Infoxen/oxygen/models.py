from django.db import models


class OxygenCylinder(models.Model):
    address = models.CharField(max_length=100)
    business_name = models.CharField(max_length=50)
    person_name = models.CharField(max_length=50, null=True)
    contact = models.BigIntegerField()
    verified_status = models.CharField(max_length= 30)
    TimeStamp = models.DateTimeField(auto_now_add=True)


