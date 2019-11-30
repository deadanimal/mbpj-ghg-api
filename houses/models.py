from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format
#from django import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#from mbpj_ghg_api.helpers import PathAndRename


from users.models import (
    CustomUser
)

class HouseType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    def __str__(self):
        return self.name



class House(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    address = models.CharField(blank=True, max_length=255)
    assessment_tax_account = models.CharField(blank=True, max_length=255)
    building_type = models.CharField(blank=True, max_length=255)
    stay_duration = models.CharField(blank=True, max_length=255)
    parmanent_occupant = models.CharField(blank=True, max_length=255)

    #house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name    


class HouseVehicle(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)

    vehicle_type = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name        

