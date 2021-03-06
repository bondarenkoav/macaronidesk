# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 19:10
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='type_notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Тип уведомления')),
                ('slug', models.SlugField(unique=True, verbose_name='Ключ')),
            ],
            options={
                'verbose_name': 'Тип ',
                'verbose_name_plural': 'Типы уведомлений ',
            },
        ),
        migrations.CreateModel(
            name='user_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок задачи')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание задачи')),
                ('limitation', models.DateTimeField(verbose_name='Срок исполнения')),
                ('high_importance', models.BooleanField(verbose_name='Высокая важность')),
                ('Create_user', models.IntegerField(verbose_name='ID автора')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('done', models.BooleanField(verbose_name='Задача выполнена')),
                ('done_description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание выполнения')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.type_notification', verbose_name='Уведомить о действиях над задачей')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'Задача ',
                'verbose_name_plural': 'Список задач ',
            },
        ),
    ]
