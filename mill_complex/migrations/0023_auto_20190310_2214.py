# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-10 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mill_complex', '0022_auto_20190310_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Crunch_TopGrade',
            field=models.CharField(choices=[('not_crunch', 'нет'), ('thereis', 'да')], max_length=50, verbose_name='Хруст в/c'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='GrainBlack',
            field=models.IntegerField(verbose_name='Черных'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='GrainBraun',
            field=models.IntegerField(verbose_name='Коричневых'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='GrainGreen',
            field=models.IntegerField(verbose_name='Зелёных'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='GrainWhite',
            field=models.IntegerField(verbose_name='Белых'),
        ),
    ]
