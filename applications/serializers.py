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
    Application,
    ApplicationAssessment,
    AssessmentAspect,
    Evaluation,
    EvaluationSchedule
)

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id']

class ApplicationAssessmentSerializer(serializers.ModelSerializer):
    supporting_doc = Base64ImageField()
    class Meta:
        model = ApplicationAssessment
        fields = '__all__'
        read_only_fields = ['id']

class AssessmentAspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentAspect
        fields = '__all__'
        read_only_fields = ['id']

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'
        read_only_fields = ['id']

class EvaluationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationSchedule
        fields = '__all__'
        read_only_fields = ['id']