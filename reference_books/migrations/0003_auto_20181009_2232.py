# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0002_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='cereal_crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('businessman', 'Индивидуальный предприниматель'), ('company', 'Организация')], max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Культура ',
                'verbose_name_plural': 'Зерновые культуры ',
            },
        ),
        migrations.RenameModel(
            old_name='provider',
            new_name='partner',
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Контрагент ', 'verbose_name_plural': 'Контрагенты '},
        ),
    ]
