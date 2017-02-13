# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-08 18:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amphi', '0002_auto_20170208_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='by'),
        ),
    ]
