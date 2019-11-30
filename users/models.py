# users/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models



#from SuperAPI.helpers import PathAndRename

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

    occupation = models.ForeignKey(UserOccupation, on_delete=models.CASCADE, null=True)

    #profile_picture = models.ImageField(null=True, upload_to=PathAndRename('images'))

    USER_TYPE = [
        ('EC', 'End Client'),
        ('AD', 'Administrator'),
        ('LO', 'Lol'),
        ('NA', 'Not Available'),   
    ]

    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        default='NA',
    )     
