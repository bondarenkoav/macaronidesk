# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept_okk', '0002_auto_20190122_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='okk_control_grain_moisture',
            options={'permissions': (('okk_cgm_list_view', 'КУЗМ. Просмотр списка'), ('okk_cgm_item_view', 'КУЗМ. Просмотр записи'), ('okk_cgm_item_add', 'КУЗМ. Добавление записи'), ('okk_cgm_item_edit', 'КУЗМ. Редактирование записи')), 'verbose_name': 'Замер ', 'verbose_name_plural': 'Контроль увлажнения зерна на мельнице (КУЗМ)'},
        ),
        migrations.AlterModelOptions(
            name='okk_operational_quality_control_flour',
            options={'permissions': (('okk_oqcf_list_view', 'ОККММ. Просмотр списка'), ('okk_oqcf_item_view', 'ОККММ. Просмотр записи'), ('okk_oqcf_item_add', 'ОККММ. Добавление записи'), ('okk_oqcf_item_edit', 'ОККММ. Редактирование записи')), 'verbose_name': 'Партия ', 'verbose_name_plural': 'Оперативный качественный контроль муки на мельнице (ОККММ)'},
        ),
        migrations.AlterModelOptions(
            name='okk_operational_quality_control_semolina',
            options={'permissions': (('okk_oqcs_list_view', 'ОККМнМ. Просмотр списка'), ('okk_oqcs_item_view', 'ОККМнМ. Просмотр записи'), ('okk_oqcs_item_add', 'ОККМнМ. Добавление записи'), ('okk_oqcs_item_edit', 'ОККМнМ. Редактирование записи')), 'verbose_name': 'Замер ', 'verbose_name_plural': 'Оперативный контроль качества манной муки (ОККМнМ)'},
        ),
        migrations.AlterModelOptions(
            name='okk_packproducts_quality_control',
            options={'permissions': (('okk_pqc_list_view', 'ККФП. Просмотр списка'), ('okk_pqc_item_view', 'ККФП. Просмотр записи'), ('okk_pqc_item_add', 'ККФП. Добавление записи'), ('okk_pqc_item_edit', 'ККФП. Редактирование записи')), 'verbose_name': 'Партия ', 'verbose_name_plural': 'Контроль качества фасованной продукции (ККФП)'},
        ),
        migrations.AlterModelOptions(
            name='okk_wheat_quality_control',
            options={'permissions': (('okk_wqc_list_view', 'ВККП. Просмотр списка'), ('okk_wqc_item_view', 'ВККП. Просмотр записи'), ('okk_wqc_item_add', 'ВККП. Добавление записи'), ('okk_wqc_item_edit', 'ВККП. Редактирование записи')), 'verbose_name': 'Партия ', 'verbose_name_plural': 'Входной контроль качества пшеницы (ВККП)'},
        ),
    ]
