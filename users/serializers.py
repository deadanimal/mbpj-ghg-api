from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers

from django.utils.timezone import now

from .models import (
    CustomUser,
    UserOccupation
)


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = 'id' ,'full_name', 'new_nric', 'old_nric', 'phone', 'email', 'gender', 'occupation', 'profile_picture', 'user_type'
        read_only_fields = ['email', 'id']

class UserOccupationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserOccupation
        fields = '__all__'
        read_only_fields = ['id']