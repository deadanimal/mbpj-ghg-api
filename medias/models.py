from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format
#from django import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from api.helpers import PathAndRename

# Create your models here.

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    image = models.ImageField(null=True, upload_to=PathAndRename('media'))