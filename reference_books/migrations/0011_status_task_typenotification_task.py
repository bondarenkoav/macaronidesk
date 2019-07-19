# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0010_auto_20190122_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='status_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Состояние')),
                ('slug', models.SlugField(unique=True, verbose_name='Ключ статуса')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет строки')),
            ],
            options={
                'verbose_name_plural': 'Статусы задач ',
                'verbose_name': 'Статус ',
            },
        ),
        migrations.CreateModel(
            name='typenotification_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Состояние')),
                ('slug', models.SlugField(unique=True, verbose_name='Ключ статуса')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет строки')),
            ],
            options={
                'verbose_name_plural': 'Варианты уведомления ',
                'verbose_name': 'Тип ',
            },
        ),
    ]