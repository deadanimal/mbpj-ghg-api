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

class Application(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='applicant')
    evaluator_nominated = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='evaluator_nominated_id')
    
    STATUS = [
        ('SN', 'Sent'),
        ('AV', 'Approved'),
        ('RJ', 'Rejected'),
        ('IP', 'In process'),
        ('EV', 'Evaluated'),
        ('PD', 'Paid'),
        ('NA', 'Not Available')
    ]

    status = models.CharField(max_length=2, choices=STATUS, default='SN')
    applied_house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, related_name='applied_house_id')
    date_submitted = models.DateField(null=True)

class ApplicationAssessment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, related_name='application_id_assessment')

    ASSESSMENT_TYPE = [
        ('EN', 'Energy'),
        ('WA', 'Water'),
        ('TR', 'Transportation'),
        ('BI', 'Biodiversity'),
        ('WE', 'Waste'),
        ('NA', 'Not Available')
    ]
    
    assessment_type = models.CharField(max_length=2, choices=ASSESSMENT_TYPE, default="NA")
    initiative = models.CharField(max_length=100, default='NA')
    improvement = models.CharField(max_length=100, default='NA')
    quantity =  models.IntegerField(default=0)
    rebate_percentage = models.IntegerField(default=0)
    supporting_doc = models.ImageField(null=True, upload_to=PathAndRename('assessment'))

    #def __str__(self):
        #return self.name

class ApplicationEvaluationAssessment(models.Model):

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

    aspect_type = models.CharField(max_length=2, choices=ASPECT_TYPE, default="NA")

    aspect = models.CharField(max_length=100, default='NA')
    incentive = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class ApplicationEvaluation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    evaluation_assessment_id = models.ForeignKey(ApplicationEvaluationAssessment, on_delete=models.CASCADE, null=True, related_name='application_assessment_id_evaluation')
    
    equipment = models.IntegerField(default=0)
    system = models.IntegerField(default=0)
    efficiency = models.IntegerField(default=0)

    remarks = models.CharField(max_length=100, default='NA')

    #def __str__(self):
        #return self.name

class ApplicationEvaluationSchedule(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, related_name='application_id_evaluation_schedule')
    date = models.DateField(null=True)
    SESSION = [
        ('AM', 'Morning'),
        ('PM', 'Evening'),
        ('NA', 'Not Available')
    ]
    session = models.CharField(max_length=2, choices=SESSION, default="NA")

    #def __str__(self):
        #return self.name