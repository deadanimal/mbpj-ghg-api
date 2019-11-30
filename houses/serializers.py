from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers


from django.utils.timezone import now




from .models import (
    House,
    HouseType
)


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = '__all__'
        read_only_fields = ['id']

class HouseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseType
        fields = '__all__'
        read_only_fields = ['id']        