# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 10:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mill_complex', '0009_auto_20190130_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mill_bagging',
            name='HandedOverBags_flour',
        ),
        migrations.RemoveField(
            model_name='mill_bagging',
            name='HandedOverBags_zelen',
        ),
        migrations.RemoveField(
            model_name='mill_bagging',
            name='HandedOverBags_zo',
        ),
    ]