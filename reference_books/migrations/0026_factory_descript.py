# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0025_auto_20190625_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='Descript',
            field=models.TextField(blank=True, verbose_name='Описание (специфика производства)'),
        ),
    ]
