# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-04 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0027_auto_20190626_1703'),
        ('auth', '0008_alter_user_username_max_length'),
        ('account', '0002_auto_20190625_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory', models.ManyToManyField(blank=True, null=True, related_name='factory_group', to='reference_books.Factory', verbose_name='Производство')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]
