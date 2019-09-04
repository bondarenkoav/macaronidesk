# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-04 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0027_auto_20190626_1703'),
        ('account', '0003_groupprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupprofile',
            name='factory',
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='factory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factory_group', to='reference_books.Factory', verbose_name='Производство'),
        ),
    ]
