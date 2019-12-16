from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format
#from django import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from api.helpers import PathAndRename

from users.models import (
    CustomUser
)

class House(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    address = models.CharField(blank=True, max_length=255)
    assessment_tax_account = models.CharField(blank=True, max_length=255)

    BUILDING_TYPE = [
        ('CD', 'Condominium'),
        ('FL', 'Flat'),
        ('TO', 'Townhouse'),
        ('TE', 'Terrace House'),
        ('BG', 'Bungalow'),
        ('SD', 'Semidetached'),
        ('AP', 'Apartment'),
        ('SA', 'Service Apartment'),
        ('OT', 'Other')
    ]

    building_type = models.CharField(max_length=2, choices=BUILDING_TYPE, default='BG')
    #stay_begin = models.DateField(null=True)
    staying_duration_years = models.IntegerField(default=0)
    staying_duration_months = models.IntegerField(default=0)
    permanent_occupant = models.IntegerField(default=0)
    vehicle_car = models.IntegerField(default=0)
    vehicle_motorcycle = models.IntegerField(default=0)
    vehicle_bicycle = models.IntegerField(default=0)
    vehicle_other = models.IntegerField(default=0)

    def __str__(self):
        return self.assessment_tax_account
