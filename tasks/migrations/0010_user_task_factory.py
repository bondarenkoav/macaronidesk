# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-27 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0027_auto_20190626_1703'),
        ('tasks', '0009_auto_20190131_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_task',
            name='Factory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reference_books.Factory', verbose_name='Организация'),
            preserve_default=False,
        ),
    ]