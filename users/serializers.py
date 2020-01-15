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
    CustomUser,
    UserOccupation,
    UserEvent
)

class CustomUserSerializer(serializers.ModelSerializer):
    nric_picture = Base64ImageField()
    profile_picture = Base64ImageField()
    class Meta:
        model = CustomUser
        fields = 'id','full_name', 'new_nric', 'old_nric', 'phone', 'tel', 'email', 'gender', 'occupation', 'nric_picture', 'profile_picture', 'user_type', 'username', 'is_active'
        read_only_fields = ['email', 'id']

class UserOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOccupation
        fields = '__all__'
        read_only_fields = ['id']

class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = '__all__'
        read_only_fields = ['id']