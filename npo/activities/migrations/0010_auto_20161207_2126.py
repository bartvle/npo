# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-07 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_auto_20160928_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-date'], 'verbose_name': 'activiteit', 'verbose_name_plural': 'activiteiten'},
        ),
    ]
