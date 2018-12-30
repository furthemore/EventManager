# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-26 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_order_apidata'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='printCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='badge',
            name='attendee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='tableSize',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.TableSize'),
        ),
        migrations.AlterField(
            model_name='dealerasst',
            name='attendee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee'),
        ),
        migrations.AlterField(
            model_name='dealerasst',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='priceLevel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.PriceLevel'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='attendee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AlterField(
            model_name='tablesize',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
    ]
