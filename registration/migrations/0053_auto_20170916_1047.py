# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-16 14:47


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0052_auto_20170715_1734"),
    ]

    operations = [
        migrations.RemoveField(model_name="jersey", name="shirtSize",),
        migrations.RemoveField(model_name="staffjersey", name="shirtSize",),
        migrations.RemoveField(model_name="attendee", name="badgeName",),
        migrations.RemoveField(model_name="attendee", name="badgeNumber",),
        migrations.RemoveField(model_name="attendee", name="badgePrinted",),
        migrations.RemoveField(model_name="attendee", name="event",),
        migrations.RemoveField(model_name="attendee", name="printed",),
        migrations.RemoveField(model_name="attendee", name="registeredDate",),
        migrations.RemoveField(model_name="attendee", name="registrationToken",),
        migrations.RemoveField(model_name="orderitem", name="attendee",),
        migrations.DeleteModel(name="Jersey",),
        migrations.DeleteModel(name="StaffJersey",),
    ]
