from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format
#from django import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from api.helpers import PathAndRename

class Faq(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    question = models.CharField(max_length=255, default='NA')
    answer = models.CharField(max_length=255, default='NA')
    date_submitted = models.DateField(null=True)

    def __str__(self):
        return self.question