# Generated by Django 2.2.6 on 2019-11-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='comment',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='mark',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
