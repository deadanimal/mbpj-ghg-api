from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers


from django.utils.timezone import now




from .models import (
    Application,
    ApplicationType
)


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id']

class ApplicationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationType
        fields = '__all__'
        read_only_fields = ['id']        