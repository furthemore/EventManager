# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-29 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0034_auto_20161227_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='contactRelation',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='staff',
            name='shirtsize',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.ShirtSizes'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='attendee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Attendee'),
        ),
    ]
