# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0017_auto_20171212_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='workout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Workout'),
        ),
    ]