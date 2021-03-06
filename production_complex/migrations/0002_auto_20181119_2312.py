# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_complex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_equipment_breakdown_repair',
            name='DateTime',
        ),
        migrations.RemoveField(
            model_name='product_line_operator',
            name='DateTime',
        ),
        migrations.RemoveField(
            model_name='product_packing_equipment_adjuster',
            name='DateTime',
        ),
        migrations.AddField(
            model_name='product_equipment_breakdown_repair',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_equipment_breakdown_repair',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_line_operator',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_line_operator',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_packing_equipment_adjuster',
            name='Date_word',
            field=models.DateField(default='2018-01-01', verbose_name='Дата контроля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_packing_equipment_adjuster',
            name='Time_word',
            field=models.TimeField(default='23:59', verbose_name='Время контроля'),
            preserve_default=False,
        ),
    ]
