# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0018_auto_20190418_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='status_machine',
            name='class_b4_td',
            field=models.SlugField(default='table-primary'),
            preserve_default=False,
        ),
    ]