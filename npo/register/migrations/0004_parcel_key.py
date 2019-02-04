# Generated by Django 2.1.1 on 2019-02-04 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20190204_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='key',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.MinLengthValidator(17), django.core.validators.MaxLengthValidator(17)], verbose_name='key'),
        ),
    ]
