# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-15 15:56


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("registration", "0085_auto_20200215_1029"),
        ("registration", "0086_auto_20200215_1051"),
    ]

    dependencies = [
        ("registration", "0084_reservedbadgenumbers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservedbadgenumbers",
            options={"verbose_name_plural": "Reserved Badge Numbers"},
        ),
        migrations.AddField(
            model_name="charity",
            name="donations",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="External donations to add to metrics",
                max_digits=12,
            ),
        ),
        migrations.AlterField(
            model_name="reservedbadgenumbers",
            name="priceLevel",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="registration.PriceLevel",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="donations",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="External donations to add to metrics ",
                max_digits=12,
            ),
        ),
    ]
