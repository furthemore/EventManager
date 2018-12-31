# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-30 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0036_staffjersey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='charityDonation',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orgDonation',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
