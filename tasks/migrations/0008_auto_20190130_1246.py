# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20190130_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_task',
            options={'permissions': (('task_list_view', 'Задачи. Просмотр списка'), ('task_item_view', 'Задачи. Просмотр записи'), ('task_item_add', 'Задачи. Добавление записи'), ('task_item_edit', 'Задачи. Редактирование записи')), 'verbose_name': 'Задача ', 'verbose_name_plural': 'Список задач '},
        ),
    ]