# Generated by Django 3.1.4 on 2020-12-08 22:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20201208_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeroute',
            name='route',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None),
        ),
    ]
