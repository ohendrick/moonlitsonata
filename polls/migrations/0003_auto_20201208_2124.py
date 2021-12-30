# Generated by Django 3.1.4 on 2020-12-08 21:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_makeroute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makeroute',
            old_name='mastered_level',
            new_name='mastery',
        ),
        migrations.RenameField(
            model_name='makeroute',
            old_name='creation_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='makeroute',
            name='route',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=40), default=1, size=21),
            preserve_default=False,
        ),
    ]