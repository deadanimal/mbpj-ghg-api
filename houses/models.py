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
    assessment_tax_doc = models.ImageField(null=True, upload_to=PathAndRename('assessment_tax'))

    BUILDING_TYPE = [
        ('CD', 'Condominium'),
        ('FL', 'Flat'),
        ('TO', 'Townhouse'),
        ('TE', 'Terrace House'),
        ('BS', 'Bungalow / Semidetached'),
        ('AS', 'Apartment / Service Apartment'),
        ('OT', 'Other')
    ]

    building_type = models.CharField(max_length=2, choices=BUILDING_TYPE, default='BG')
    staying_duration_years = models.IntegerField(default=0)
    staying_duration_months = models.IntegerField(default=0)
    permanent_occupant = models.IntegerField(default=0)
    vehicle_car = models.IntegerField(default=0)
    vehicle_motorcycle = models.IntegerField(default=0)
    vehicle_bicycle = models.IntegerField(default=0)
    vehicle_other = models.IntegerField(default=0)

    electricity_bill_1_month = models.CharField(max_length=100, default='NA')
    electricity_bill_1_usage = models.IntegerField(default=0)
    electricity_bill_1_doc = models.ImageField(null=True, upload_to=PathAndRename('bills'))
    electricity_bill_2_month = models.CharField(max_length=100, default='NA')
    electricity_bill_2_usage = models.IntegerField(default=0)
    electricity_bill_2_doc = models.ImageField(null=True, upload_to=PathAndRename('bills'))
    electricity_bill_3_month = models.CharField(max_length=100, default='NA')
    electricity_bill_3_usage = models.IntegerField(default=0)
    electricity_bill_3_doc = models.ImageField(null=True, upload_to=PathAndRename('bills'))

    water_bill_1_month = models.CharField(max_length=100, default='NA')
    water_bill_1_usage = models.IntegerField(default=0)
    water_bill_1_doc = models.ImageField(null=True, upload_to=PathAndRename('bills'))
    water_bill_2_month = models.CharField(max_length=100, default='NA')
    water_bill_2_usage = models.IntegerField(default=0)
    water_bill_2_doc = models.ImageField(null=True, upload_to=PathAndRename('bills'))
    water_bill_3_month = models.CharField(max_length=100, default='NA')
    water_bill_3_usage = models.IntegerField(default=0)
    water_bill_3_doc = models.ImageField(null=True, upload_to=PathAndRename('bills'))

    def __str__(self):
        return self.assessment_tax_account

class HouseEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    action = models.CharField(max_length=100, default='NA')
    action_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='house_event_by')
    date_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_time']
