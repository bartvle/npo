# Generated by Django 3.1.7 on 2021-03-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amphi', '0005_auto_20210220_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='location',
            field=models.IntegerField(choices=[(1, 'Lembergestraat'), (2, 'Hoek ter Hulst'), (3, 'Turkenhoek')], verbose_name='location'),
        ),
    ]
