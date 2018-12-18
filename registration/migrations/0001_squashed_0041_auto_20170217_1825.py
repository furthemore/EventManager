# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-17 02:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    replaces = [(b'registration', '0001_initial'), (b'registration', '0002_auto_20160726_2342'), (b'registration', '0003_auto_20160727_0114'), (b'registration', '0004_auto_20160729_0021'), (b'registration', '0005_auto_20160806_1650'), (b'registration', '0006_auto_20160806_1733'), (b'registration', '0007_auto_20160821_1554'), (b'registration', '0008_auto_20160821_1600'), (b'registration', '0009_auto_20160821_1340'), (b'registration', '0010_auto_20160828_1010'), (b'registration', '0011_auto_20160830_2149'), (b'registration', '0012_auto_20160830_2154'), (b'registration', '0013_auto_20160917_1045'), (b'registration', '0014_auto_20160926_1925'), (b'registration', '0015_auto_20160926_1927'), (b'registration', '0016_priceleveloption_required'), (b'registration', '0017_auto_20161009_1154'), (b'registration', '0018_auto_20161010_1838'), (b'registration', '0019_auto_20161013_1813'), (b'registration', '0020_remove_dealer_extratable'), (b'registration', '0021_auto_20161013_1941'), (b'registration', '0022_auto_20161020_1832'), (b'registration', '0023_auto_20161020_1843'), (b'registration', '0024_auto_20161020_1910'), (b'registration', '0025_tablesize_baseprice'), (b'registration', '0026_dealer_buttonoffer'), (b'registration', '0027_auto_20161104_2004'), (b'registration', '0028_order_status'), (b'registration', '0029_dealer_emailed'), (b'registration', '0030_auto_20161221_1121'), (b'registration', '0031_auto_20161223_1717'), (b'registration', '0032_auto_20161223_1732'), (b'registration', '0033_discount_used'), (b'registration', '0034_auto_20161227_1230'), (b'registration', '0035_auto_20161228_1940'), (b'registration', '0036_staffjersey'), (b'registration', '0037_auto_20161230_1154'), (b'registration', '0038_auto_20170128_1001'), (b'registration', '0039_auto_20170129_1410'), (b'registration', '0040_staffjersey'), (b'registration', '0041_auto_20170217_1825')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('postalCode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('badgeName', models.CharField(blank=True, max_length=200)),
                ('badgeNumber', models.IntegerField(null=True)),
                ('badgePrinted', models.BooleanField(default=False)),
                ('emailsOk', models.BooleanField(default=False)),
                ('volunteerContact', models.BooleanField(default=False)),
                ('volunteerDepts', models.CharField(max_length=1000)),
                ('notes', models.TextField()),
                ('parentFirstName', models.CharField(blank=True, max_length=200)),
                ('parentLastName', models.CharField(blank=True, max_length=200)),
                ('parentPhone', models.CharField(blank=True, max_length=20)),
                ('parentEmail', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AttendeeOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionExtraValue', models.CharField(max_length=200)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee')),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('volunteerListOk', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=100)),
                ('percentOff', models.IntegerField(null=True)),
                ('amountOff', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('attendeeRegEnd', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 29, 14, 919844))),
                ('attendeeRegStart', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 29, 33, 273653))),
                ('dealerRegEnd', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 30, 2, 634132))),
                ('dealerRegStart', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 30, 9, 48132))),
                ('onlineRegEnd', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 30, 13, 626466))),
                ('onlineRegStart', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 30, 18, 265170))),
                ('staffRegEnd', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 30, 22, 617158))),
                ('staffRegStart', models.DateTimeField(default=datetime.datetime(2016, 12, 27, 12, 30, 28, 51655))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HoldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('authorizationCode', models.CharField(max_length=100)),
                ('transactionId', models.CharField(max_length=100)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('settledDate', models.DateTimeField(null=True)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmationCode', models.CharField(max_length=100)),
                ('enteredBy', models.CharField(max_length=100)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee')),
                ('discount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Discount')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PriceLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('basePrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('public', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceLevelOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionName', models.CharField(max_length=200)),
                ('optionPrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('optionExtraType', models.CharField(blank=True, max_length=100)),
                ('priceLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.PriceLevel')),
                ('required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShirtSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.ShirtSizes')),
                ('contactName', models.CharField(blank=True, max_length=200)),
                ('contactPhone', models.CharField(blank=True, max_length=200)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Department')),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('needRoom', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('registrationToken', models.CharField(default=registration.models.getRegistrationToken, max_length=200)),
                ('specialFood', models.TextField(blank=True)),
                ('specialMedical', models.TextField(blank=True)),
                ('specialSkills', models.TextField(blank=True)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Staff')),
                ('telegram', models.CharField(blank=True, max_length=200)),
                ('timesheetAccess', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('twitter', models.CharField(blank=True, max_length=200)),
                ('contactRelation', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='priceLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.PriceLevel'),
        ),
        migrations.AddField(
            model_name='attendeeoptions',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.PriceLevelOption'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='holdType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.HoldType'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Attendee'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='volunteerDepts',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='badgeNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.RenameField(
            model_name='order',
            old_name='createdDate',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='authorizationCode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='order',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='order',
            name='settledDate',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transactionId',
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.RemoveField(
            model_name='attendeeoptions',
            name='attendee',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='attendee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee'),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='discount',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Order'),
        ),
        migrations.AddField(
            model_name='attendeeoptions',
            name='orderItem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registration.OrderItem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Attendee'),
        ),
        migrations.RenameField(
            model_name='attendeeoptions',
            old_name='optionExtraValue',
            new_name='optionValue',
        ),
        migrations.AddField(
            model_name='order',
            name='charityDonation',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='orgDonation',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.AddField(
            model_name='attendee',
            name='registeredDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='reference',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='settledDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='enteredDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billingAddress1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='billingAddress2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='billingCity',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='billingCountry',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='billingEmail',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='billingName',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='billingPostal',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='billingState',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TableSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('chairMax', models.IntegerField(default=1)),
                ('chairMin', models.IntegerField(default=1)),
                ('tableMax', models.IntegerField(default=0)),
                ('tableMin', models.IntegerField(default=0)),
                ('partnerMax', models.IntegerField(default=1)),
                ('partnerMin', models.IntegerField(default=1)),
                ('basePrice', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dealer',
            name='attendee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Attendee'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='businessName',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='farFrom',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='dealer',
            name='license',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='nearTo',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='dealer',
            name='needPower',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='needWifi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='registrationToken',
            field=models.CharField(default=registration.models.getRegistrationToken, max_length=200),
        ),
        migrations.AddField(
            model_name='dealer',
            name='tableNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='wallSpace',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='website',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Jersey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=3)),
                ('shirtSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.ShirtSizes')),
            ],
        ),
        migrations.AddField(
            model_name='dealer',
            name='agreeToRules',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='artShow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='chairs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dealer',
            name='charityRaffle',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='reception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='tableSize',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.TableSize'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='breakfast',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='willSwitch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dealer',
            name='partners',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='tables',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dealer',
            name='buttonOffer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='dealer',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='dealer',
            name='discountReason',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AddField(
            model_name='dealer',
            name='emailed',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='confirmationCode',
        ),
        migrations.AddField(
            model_name='pricelevel',
            name='group',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='registrationToken',
            field=models.CharField(default=registration.models.getRegistrationToken, max_length=200),
        ),
        migrations.AddField(
            model_name='discount',
            name='oneTime',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discount',
            name='reason',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='discount',
            name='used',
            field=models.IntegerField(default=0),
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
        migrations.CreateModel(
            name='StaffJersey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=3)),
                ('shirtSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.ShirtSizes')),
            ],
        ),
    ]