# Generated by Django 3.1.4 on 2021-02-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20201003_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='info',
            field=models.TextField(blank=True, verbose_name='information'),
        ),
    ]
