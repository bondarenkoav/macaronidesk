# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_okk', '0007_auto_20190605_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='okk_operational_quality_control_semolina',
            name='Productivity',
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='Acidity',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Кислотность, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='AshContent',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Зольность, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='Foramen',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Проход, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='Gluten',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Клейковина отмытая вручную, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='GlutenInfratek',
            field=models.IntegerField(verbose_name='Клейковина/Инфратек, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='IDK',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='ИДК, усл.ед.'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='MetalImpurity',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Металлопримесь, мг/кг'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='MoistureInfratek',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Влажность/Инфратек, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='Productivity',
            field=models.IntegerField(verbose_name='Производительность, кг/час'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='Protein',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Белок, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_flour',
            name='Residue',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Остаток, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_semolina',
            name='Foramen',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Проход, %'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_semolina',
            name='MetalImpurity',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Металлопримесь, мг/кг'),
        ),
        migrations.AlterField(
            model_name='okk_operational_quality_control_semolina',
            name='Moisture',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Влажность, %'),
        ),
    ]
