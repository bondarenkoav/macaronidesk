# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-28 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mill_complex', '0007_auto_20190122_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mill_grain_waste_accounting',
            options={'permissions': (('m_gwa_list_view', 'УЗО. Просмотр списка'), ('m_gwa_item_view', 'УЗО. Просмотр записи'), ('m_gwa_item_add', 'УЗО. Добавление записи'), ('m_gwa_item_edit', 'УЗО. Редактирование записи')), 'verbose_name': 'Смена ', 'verbose_name_plural': 'Учёт зерноотходов (УЗО)'},
        ),
        migrations.RemoveField(
            model_name='mill_grain_waste_accounting',
            name='Assistant',
        ),
        migrations.RemoveField(
            model_name='mill_grain_waste_accounting',
            name='Dust',
        ),
        migrations.RemoveField(
            model_name='mill_grain_waste_accounting',
            name='KnockedOut',
        ),
        migrations.RemoveField(
            model_name='mill_grain_waste_accounting',
            name='Supervisor',
        ),
        migrations.RemoveField(
            model_name='mill_laboratory_work',
            name='BAKBHM',
        ),
        migrations.RemoveField(
            model_name='mill_laboratory_work',
            name='Inclusion_Black',
        ),
        migrations.RemoveField(
            model_name='mill_laboratory_work',
            name='Inclusion_Brown',
        ),
        migrations.RemoveField(
            model_name='mill_laboratory_work',
            name='SieveResidue125',
        ),
        migrations.RemoveField(
            model_name='mill_laboratory_work',
            name='SieveResidue245',
        ),
        migrations.AddField(
            model_name='mill_grain_waste_accounting',
            name='Bran2Varieties',
            field=models.IntegerField(default=0, verbose_name='Отруби 2сорта, кг.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_grain_waste_accounting',
            name='GrainWaste',
            field=models.IntegerField(default=0, verbose_name='Зерноотходы, кг.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Bran_Nature',
            field=models.IntegerField(default=0, verbose_name='Отруби натура, г/л'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Crunch_TopGrade',
            field=models.CharField(choices=[('not_crunch', 'Нет'), ('thereis', 'Есть')], default=0, max_length=50, verbose_name='Хруст в/c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='MetalImpurity_TopGrade',
            field=models.CharField(choices=[('not_metal', 'Нет примеси'), ('thereis', '1мг')], default=0, max_length=50, verbose_name='Металлопримесь в/c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Passage_GradeSecond',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Проход в/c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Passage_TopGrade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Проход в/c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Remainder_GradeSecond',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Остаток 2ой сорт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Remainder_TopGrade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Остаток в/с'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_laboratory_work',
            name='Yellowish_TopGrade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Желтизна в/c'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mill_bagging',
            name='Gang',
            field=models.CharField(choices=[('day_shift', 'Смена дневная'), ('night_shift', 'Смена ночная')], max_length=30, verbose_name='Смена'),
        ),
        migrations.AlterField(
            model_name='mill_grain_waste_accounting',
            name='Gang',
            field=models.CharField(choices=[('day_shift', 'Смена дневная'), ('night_shift', 'Смена ночная')], max_length=30, verbose_name='Смена'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Grade_Second',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Второй сорт'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Grade_Top',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Высший сорт'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Postponing_One',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Отлёжка 1'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Postponing_Three',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Отлёжка 3'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Postponing_Two',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Отлёжка 2'),
        ),
        migrations.AlterField(
            model_name='mill_laboratory_work',
            name='Verifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.coworker', verbose_name='Смена'),
        ),
    ]
