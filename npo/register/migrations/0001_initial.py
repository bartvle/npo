# Generated by Django 2.1.1 on 2019-02-04 19:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('address', models.CharField(blank=True, max_length=80, verbose_name='address')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=40, verbose_name='phone')),
            ],
            options={
                'verbose_name_plural': 'owners',
                'verbose_name': 'owner',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Owner', verbose_name='owner')),
            ],
            options={
                'verbose_name_plural': 'ownerships',
                'verbose_name': 'ownership',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(17), django.core.validators.MaxLengthValidator(17)], verbose_name='capakey')),
                ('owners', models.ManyToManyField(through='register.Ownership', to='register.Owner')),
            ],
            options={
                'verbose_name_plural': 'parcels',
                'verbose_name': 'parcel',
            },
        ),
        migrations.AddField(
            model_name='ownership',
            name='parcel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Parcel', verbose_name='parcel'),
        ),
    ]
