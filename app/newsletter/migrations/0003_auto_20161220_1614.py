# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-20 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20161207_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['email'], 'verbose_name': 'inschrijving', 'verbose_name_plural': 'inschrijvingen'},
        ),
    ]