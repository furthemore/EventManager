# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-23 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_auto_20161223_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='used',
            field=models.IntegerField(default=0),
        ),
    ]