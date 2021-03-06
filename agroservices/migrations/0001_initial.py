# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, null=True)),
                ('quantitystock', models.IntegerField()),
                ('unitmeasurement', models.CharField(blank=True, choices=[('KG', 'Kilograma'), ('L', 'Litros'), ('ha', 'hectares'), ('m', 'metros')], max_length=2, verbose_name='Unidade')),
                ('unitprice', models.FloatField()),
                ('averageprice', models.FloatField()),
                ('lastupdate', models.DateField(auto_now=True)),
            ],
        ),
    ]
