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

class TicketQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    question = models.CharField(max_length=255, default='NA')
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='question_by')

    STATUS = [
        ('RS', 'Resolved'),
        ('UR', 'Unresolved'),
        ('OT', 'Other')
    ]

    status = models.CharField(max_length=2, choices=STATUS, default='UR')
    date_submitted = models.DateField(null=True)

    class Meta:
        ordering = ['-status', '-date_submitted']

class TicketAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    question_id = models.ForeignKey(TicketQuestion, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=255, default='NA')
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='answer_by')
    date_submitted = models.DateField(null=True)

    class Meta:
        ordering = ['-date_submitted']

class TicketEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    action = models.CharField(max_length=100, default='NA')
    action_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='ticket_event_by')
    date_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_time']