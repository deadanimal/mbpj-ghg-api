# users/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from api.helpers import PathAndRename

class UserOccupation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(blank=True, max_length=255)
    
    new_nric = models.CharField(blank=True, max_length=255)
    old_nric = models.CharField(blank=True, max_length=255)

    phone = models.CharField(blank=True, max_length=255)
    tel = models.CharField(blank=True,max_length=255)
    email = models.CharField(blank=True, max_length=255)
    
    GENDER_TYPE = [
        ('ML', 'Male'),
        ('FM', 'Female'),
        ('NA', 'Not Available')
    ]

    gender = models.CharField(max_length=2, choices=GENDER_TYPE, default='NA')
    occupation = models.ForeignKey(UserOccupation, on_delete=models.CASCADE, null=True)

    USER_TYPE = [
        ('AP', 'Applicant'),
        ('EV', 'Evaluator'),
        ('AD', 'Administrator'),
        ('NA', 'Not Available'),
    ]

    user_type = models.CharField(max_length=2, choices=USER_TYPE, default='AP')
    profile_picture = models.ImageField(null=True, upload_to=PathAndRename('images'))