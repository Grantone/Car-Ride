# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liscence_no', models.CharField(max_length=30, verbose_name='liscence_no')),
                ('scanned', models.ImageField(blank=True, upload_to='', verbose_name="picture of driver's liscence")),
                ('confirmed', models.BooleanField(default=False, verbose_name='confirmed')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('work', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.CharField(max_length=256, verbose_name='pick up point')),
                ('dest', models.CharField(max_length=256, verbose_name='destination')),
                ('status', models.CharField(default='pending', max_length=256, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=160, verbose_name='vehicle make')),
                ('plate', models.CharField(max_length=15, verbose_name='liscenced plate number')),
                ('seats', models.IntegerField(verbose_name='no of seats')),
                ('type', models.CharField(max_length=30, verbose_name='vehicle type')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=60)),
                ('cost', models.IntegerField()),
                ('start_time', models.TimeField(max_length=60)),
                ('no_pass', models.IntegerField(verbose_name='no of passengers')),
                ('ended', models.BooleanField(default=False, verbose_name='sharing ended')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.Vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.Vehicle'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
