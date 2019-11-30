from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format
#from django import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#from mbpj_ghg_api.helpers import PathAndRename


from users.models import (
    CustomUser
)

class AssessmentType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    ASSESSMENT_GROUP = [
        ('NA', 'Not Available'),   
    ]

    assessment_group = models.CharField(
        max_length=2,
        choices=ASSESSMENT_GROUP,
        default='NA',
    )     

    max_rebate = models.IntegerField(default=0)

    def __str__(self):
        return self.assessment_group


class Assessment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    assessment_type = models.ForeignKey(AssessmentType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name    

class AssessmentDetail(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    aspect = models.CharField(max_length=100, default='NA')
    initiative = models.CharField(max_length=100, default='NA')
    improvement = models.CharField(max_length=100, default='NA')
    quantity = models.CharField(max_length=100, default='NA')
    rebate = models.CharField(max_length=100, default='NA')

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name            

