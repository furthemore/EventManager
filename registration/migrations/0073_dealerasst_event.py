# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-22 01:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0072_dealerasst'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealerasst',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Event'),
        ),
    ]
