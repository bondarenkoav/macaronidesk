# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0008_auto_20181205_2353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cereal_crop',
            options={'permissions': (('list_view', 'Зерновые культуры. Просмотр списка'), ('item_view', 'Зерновые культуры. Просмотр записи'), ('item_add', 'Зерновые культуры. Добавление записи'), ('item_edit', 'Зерновые культуры. Редактирование записи')), 'verbose_name': 'Культура ', 'verbose_name_plural': 'Зерновые культуры '},
        ),
        migrations.AlterModelOptions(
            name='coworker',
            options={'permissions': (('list_view', 'Список исполнителей. Просмотр списка'), ('item_view', 'Список исполнителей. Просмотр записи'), ('item_add', 'Список исполнителей. Добавление записи'), ('item_edit', 'Список исполнителей. Редактирование записи')), 'verbose_name': 'Исполнитель/Сотрудник ', 'verbose_name_plural': 'Список исполнителей '},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'permissions': (('list_view', 'Контрагенты. Просмотр списка'), ('item_view', 'Контрагенты. Просмотр записи'), ('item_add', 'Контрагенты. Добавление записи'), ('item_edit', 'Контрагенты. Редактирование записи')), 'verbose_name': 'Контрагент ', 'verbose_name_plural': 'Контрагенты '},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'permissions': (('list_view', 'Продукция. Просмотр списка'), ('item_view', 'Продукция. Просмотр записи'), ('item_add', 'Продукция. Добавление записи'), ('item_edit', 'Продукция. Редактирование записи')), 'verbose_name': 'Вид ', 'verbose_name_plural': 'Продукция '},
        ),
    ]