# Generated by Django 3.1.4 on 2020-12-08 21:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_makeroute_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeroute',
            name='route',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=3),
        ),
    ]
