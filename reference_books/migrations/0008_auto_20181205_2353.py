# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0007_machine_production'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вид ',
                'verbose_name_plural': 'Продукция ',
            },
        ),
        migrations.DeleteModel(
            name='pasta',
        ),
    ]
