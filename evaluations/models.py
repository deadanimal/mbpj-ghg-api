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

class EvaluationType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    def __str__(self):
        return self.name


class Evaluation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, default='NA')

    mark = models.CharField(max_length=100, default='NA')
    comment = models.CharField(max_length=100, default='NA')

    evaluation_date = models.DateTimeField(null=True)
    evaluation_type = models.ForeignKey(EvaluationType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name    

