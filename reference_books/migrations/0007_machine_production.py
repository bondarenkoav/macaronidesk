# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0006_auto_20181105_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine_production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Станок ',
                'verbose_name_plural': 'Станки для производства макарон ',
            },
        ),
    ]
