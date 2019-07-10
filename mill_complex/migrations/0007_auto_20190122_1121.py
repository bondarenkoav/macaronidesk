# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mill_complex', '0006_auto_20190122_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elevator_shipment_wheat_to_mill',
            options={'permissions': (('m_eswm_list_view', 'ОПМ. Просмотр списка'), ('m_eswm_item_view', 'ОПМ. Просмотр записи'), ('m_eswm_item_add', 'ОПМ. Добавление записи'), ('m_eswm_item_edit', 'ОПМ. Редактирование записи')), 'verbose_name': 'Партия ', 'verbose_name_plural': 'Отгрузка пшеницы на мельницу (ОПМ)'},
        ),
        migrations.AlterModelOptions(
            name='mill_bagging',
            options={'permissions': (('m_bag_list_view', 'Учет мешков. Просмотр списка'), ('m_bag_item_view', 'Учет мешков. Просмотр записи'), ('m_bag_item_add', 'Учет мешков. Добавление записи'), ('m_bag_item_edit', 'Учет мешков. Редактирование записи')), 'verbose_name': 'Смена ', 'verbose_name_plural': 'Учёт мешков'},
        ),
        migrations.AlterModelOptions(
            name='mill_control_magnetic_installations',
            options={'permissions': (('m_cmi_list_view', 'КМУ. Просмотр списка'), ('m_cmi_item_view', 'КМУ. Просмотр записи'), ('m_cmi_item_add', 'КМУ. Добавление записи'), ('m_cmi_item_edit', 'КМУ. Редактирование записи')), 'verbose_name': 'Смена ', 'verbose_name_plural': 'Контроль магнитных установок (КМУ)'},
        ),
        migrations.AlterModelOptions(
            name='mill_grain_waste_accounting',
            options={'permissions': (('m_gwa_list_view', 'УЗО. Просмотр списка'), ('m_gwa_item_view', 'УЗО. Просмотр записи'), ('m_gwa_item_add', 'УЗО. Добавление записи'), ('m_gwa_item_edit', 'УЗО. Редактирование записи')), 'verbose_name': 'Смена ', 'verbose_name_plural': 'Учёт зерна/отходов (УЗО)'},
        ),
        migrations.AlterModelOptions(
            name='mill_laboratory_work',
            options={'permissions': (('m_lw_list_view', 'ЖЛр. Просмотр списка'), ('m_lw_item_view', 'ЖЛр. Просмотр записи'), ('m_lw_item_add', 'ЖЛр. Добавление записи'), ('m_lw_item_edit', 'ЖЛр. Редактирование записи')), 'verbose_name': 'Смена ', 'verbose_name_plural': 'Журнал лабораторных работ (ЖЛр)'},
        ),
    ]
