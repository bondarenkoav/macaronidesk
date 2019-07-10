# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Ключ категории')),
                ('icon', models.CharField(blank=True, help_text='Допустим: search', max_length=10, verbose_name='Класс иконки bootstrap4')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='dashboard.menu', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Ветка меню ',
                'verbose_name_plural': 'Дерево меню ',
            },
        ),
    ]
