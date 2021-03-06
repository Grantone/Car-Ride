# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ride', '0002_auto_20171208_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liscence_no', models.CharField(max_length=30, verbose_name='liscence_no')),
                ('scanned', models.ImageField(blank=True, upload_to='', verbose_name="picture of driver's liscence")),
                ('car_picture', models.ImageField(upload_to='pictures/')),
                ('number_plates', models.CharField(max_length=30)),
                ('capacity', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=30)),
                ('city', models.CharField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='user',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
    ]
