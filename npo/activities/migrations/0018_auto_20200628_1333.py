# Generated by Django 2.2.5 on 2020-06-28 11:33

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0017_auto_20200628_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='practical',
            field=djrichtextfield.models.RichTextField(verbose_name='practical'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='short',
            field=djrichtextfield.models.RichTextField(max_length=150, verbose_name='short'),
        ),
    ]
