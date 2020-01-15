from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    TicketAnswer,
    TicketQuestion,
    TicketEvent
)

class TicketAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAnswer
        fields = '__all__'
        read_only_fields = ['id']

class TicketQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketQuestion
        fields = '__all__'
        read_only_fields = ['id']

class TicketEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketEvent
        fields = '__all__'
        read_only_fields = ['id']