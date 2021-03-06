# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0011_status_task_typenotification_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='BHM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Состояние')),
                ('slug', models.SlugField(unique=True, verbose_name='Ключ статуса')),
            ],
            options={
                'verbose_name_plural': 'Установки БХМ ',
                'verbose_name': 'БХМ ',
            },
        ),
    ]
