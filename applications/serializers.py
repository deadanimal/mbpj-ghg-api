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
    ApplicationAssessment,
    ApplicationEvaluation,
    ApplicationEvaluationAssessment,
    ApplicationEvaluationSchedule
)

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id']

class ApplicationAssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationAssessment
        fields = '__all__'
        read_only_fields = ['id']

class ApplicationEvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationEvaluation
        fields = '__all__'
        read_only_fields = ['id']

class ApplicationEvaluationAssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationEvaluationAssessment
        fields = '__all__'
        read_only_fields = ['id']

class ApplicationEvaluationScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationEvaluationSchedule
        fields = '__all__'
        read_only_fields = ['id']