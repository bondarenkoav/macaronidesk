# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0008_auto_20181205_2353'),
        ('production_complex', '0004_auto_20181212_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_work_plan',
            name='equipement',
        ),
        migrations.AddField(
            model_name='product_work_plan',
            name='equipement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference_books.machine_production', verbose_name='Оборудование'),
        ),
    ]
