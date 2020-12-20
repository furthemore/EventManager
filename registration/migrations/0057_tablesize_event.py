# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 23:55


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0056_dealer_asstbreakfast"),
    ]

    operations = [
        migrations.AddField(
            model_name="tablesize",
            name="event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="registration.Event",
            ),
        ),
    ]
