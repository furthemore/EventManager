# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-17 23:25


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0040_staffjersey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendee",
            name="registeredDate",
            field=models.DateTimeField(null=True),
        ),
    ]
