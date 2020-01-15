from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from django.utils.timezone import now

from .models import (
    House,
    HouseEvent
)

class HouseSerializer(serializers.ModelSerializer):
    assessment_tax_doc = Base64ImageField()
    electricity_bill_1_doc = Base64ImageField()
    electricity_bill_2_doc = Base64ImageField()
    electricity_bill_3_doc = Base64ImageField()
    water_bill_1_doc = Base64ImageField()
    water_bill_2_doc = Base64ImageField()
    water_bill_3_doc = Base64ImageField()
    class Meta:
        model = House
        fields = '__all__'
        read_only_fields = ['id']

class HouseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseEvent
        fields = '__all__'
        read_only_fields = ['id']