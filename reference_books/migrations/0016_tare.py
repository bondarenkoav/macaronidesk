# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0015_auto_20190218_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='tare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Тара ',
                'verbose_name': 'вид ',
            },
        ),
    ]