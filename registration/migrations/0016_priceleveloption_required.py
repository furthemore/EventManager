# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-06 00:53


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0015_auto_20160926_1927"),
    ]

    operations = [
        migrations.AddField(
            model_name="priceleveloption",
            name="required",
            field=models.BooleanField(default=False),
        ),
    ]
