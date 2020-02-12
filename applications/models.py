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

from houses.models import (
    House
)

class AssessmentAspect(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    ASPECT_TYPE = [
        ('EN', 'Energy'),
        ('WA', 'Water'),
        ('TR', 'Transportation'),
        ('BI', 'Biodiversity'),
        ('WE', 'Waste'),
        ('NA', 'Not Available')
    ]

    aspect_type = models.CharField(max_length=2, choices=ASPECT_TYPE, default='NA')

    aspect = models.CharField(max_length=100, default='NA')
    incentive = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='application_applicant')
    evaluator_nominated = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='application_evaluator_nominated')
    
    STATUS = [
        ('CM', 'Completed'),
        ('CR', 'Created'),
        ('IE', 'In Evaluation'),
        ('IP', 'In Progress'),
        ('NA', 'Not Available'),
        ('PD', 'Paid'),
        ('RJ', 'Rejected'),
        ('SM', 'Submitted')
    ]

    status = models.CharField(max_length=2, choices=STATUS, default='CR')
    applied_house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, related_name='applied_house_id')
    date_submitted = models.DateField(null=True)

    class Meta:
        ordering = ['-date_submitted']

class ApplicationAssessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, related_name='application_assessment_application')
    assessment_aspect = models.ForeignKey(AssessmentAspect, on_delete=models.CASCADE, null=True, related_name='application_assessment_assessment_aspect')
    remarks = models.CharField(max_length=255, default='NA')
    supporting_doc = models.ImageField(null=True, upload_to=PathAndRename('assessment'))

    #def __str__(self):
        #return self.name

class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    application_assessment = models.ForeignKey(ApplicationAssessment, on_delete=models.CASCADE, null=True, related_name='evaluation_application_assessment')
    
    equipment = models.IntegerField(default=0)
    system = models.IntegerField(default=0)
    efficiency = models.IntegerField(default=0)

    remarks = models.CharField(max_length=255, default='NA')

    #def __str__(self):
        #return self.name

class EvaluationSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, related_name='evaluation_schedule_application')
    date = models.DateField(null=True)

    SESSION = [
        ('AM', 'Morning'),
        ('PM', 'Evening'),
        ('NA', 'Not Available')
    ]

    session = models.CharField(max_length=2, choices=SESSION, default='NA')

    #def __str__(self):
        #return self.name
    
    class Meta:
        ordering = ['-date']

class ApplicationEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    action = models.CharField(max_length=100, default='NA')
    action_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='application_event_by')
    date_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_time']