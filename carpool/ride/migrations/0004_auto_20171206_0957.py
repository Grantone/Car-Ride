# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 06:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ride', '0003_auto_20171206_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='user',
        ),
        migrations.AddField(
            model_name='passenger',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
