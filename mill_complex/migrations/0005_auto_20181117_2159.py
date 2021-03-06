# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-17 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mill_complex', '0004_auto_20181117_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elevator_shipment_wheat_to_mill',
            name='DateTime_word',
        ),
        migrations.RemoveField(
            model_name='mill_bagging',
            name='DateTime_word',
        ),
        migrations.RemoveField(
            model_name='mill_control_magnetic_installations',
            name='DateTime_word',
        ),
        migrations.RemoveField(
            model_name='mill_grain_waste_accounting',
            name='DateTime_word',
        ),
        migrations.RemoveField(
            model_name='mill_laboratory_work',
            name='DateTime_word',
        ),
        migrations.AddField(
            model_name='elevator_shipment_wheat_to_mill',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elevator_shipment_wheat_to_mill',
            name='Time_word',
            field=models.TimeField(default='00:00', verbose_name='Время контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_bagging',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_bagging',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_control_magnetic_installations',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_control_magnetic_installations',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_grain_waste_accounting',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_grain_waste_accounting',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
    ]
