# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_user_task_factory'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_task',
            name='confirmation',
            field=models.BooleanField(default=False, verbose_name='Подтверждение'),
        ),
    ]
