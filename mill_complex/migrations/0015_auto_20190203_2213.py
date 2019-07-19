# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0013_auto_20190201_1608'),
        ('mill_complex', '0014_auto_20190203_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mill_technological_child_bhm',
            name='BHM',
        ),
        migrations.AddField(
            model_name='mill_technological_child_bhm',
            name='bhm_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference_books.BHM', verbose_name='БХМ №'),
        ),
        migrations.AddField(
            model_name='mill_technological_child_bhm',
            name='grain',
            field=models.IntegerField(default=100, verbose_name='%'),
            preserve_default=False,
        ),
    ]