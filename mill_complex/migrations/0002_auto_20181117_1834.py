# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-17 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mill_complex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator_shipment_wheat_to_mill',
            name='Yellowish',
            field=models.IntegerField(help_text='Указывается в %', verbose_name='Желтизна'),
        ),
    ]
