# Generated by Django 2.2.6 on 2019-12-18 10:31

import api.helpers
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to=api.helpers.PathAndRename('media'))),
            ],
        ),
    ]
