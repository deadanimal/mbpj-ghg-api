# Generated by Django 2.2.6 on 2020-02-12 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rebates', '0003_auto_20191211_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rebate',
            options={'ordering': ['-payment_date']},
        ),
    ]
