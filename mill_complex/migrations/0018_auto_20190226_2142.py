# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 16:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0016_tare'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mill_complex', '0017_auto_20190218_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='elevator_grain_intake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('CarNumber', models.CharField(max_length=100, verbose_name='Гос.номер автомобиля')),
                ('WeightGross', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Вес брутто, кг')),
                ('WeightTare', models.IntegerField(verbose_name='Вес тары, кг')),
                ('WeightNet', models.IntegerField(verbose_name='Вес нетто, кг')),
                ('WeightActual', models.IntegerField(verbose_name='Вес фактический, кг')),
                ('WeightCredit', models.IntegerField(verbose_name='Вес зачетный, кг')),
                ('Comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('CerealCrop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.cereal_crop', verbose_name='Зерновая культура')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_egi_creator', to=settings.AUTH_USER_MODEL)),
                ('Provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.partner', verbose_name='Контрагент')),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_egi_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('m_egi_list_view', 'УПЗ. Просмотр списка'), ('m_egi_item_view', 'УПЗ. Просмотр записи'), ('m_egi_item_add', 'УПЗ. Добавление записи'), ('m_egi_item_edit', 'УПЗ. Редактирование записи')),
                'verbose_name_plural': 'Учет прихода зерна (УПЗ)',
                'verbose_name': 'Партия ',
            },
        ),
        migrations.CreateModel(
            name='elevator_grain_waste_accounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('GrainWaste', models.IntegerField(verbose_name='Зерноотходы, кг.')),
                ('GrainWasteSecondGrade', models.IntegerField(verbose_name='Зерноотходы 2сорта, кг.')),
                ('Comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_egwa_creator', to=settings.AUTH_USER_MODEL)),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_egwa_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('m_egwa_list_view', 'ЭУЗО. Просмотр списка'), ('m_egwa_item_view', 'ЭУЗО. Просмотр записи'), ('m_egwa_item_add', 'ЭУЗО. Добавление записи'), ('m_egwa_item_edit', 'ЭУЗО. Редактирование записи')),
                'verbose_name_plural': 'Учёт зерноотходов на элеваторе (ЭУЗО)',
                'verbose_name': 'Партия ',
            },
        ),
        migrations.CreateModel(
            name='mill_storage_flour_accounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('TopGrade', models.IntegerField(verbose_name='Высший сорт, кг')),
                ('SecondGrade', models.IntegerField(verbose_name='Второй сорт, кг')),
                ('TransportTopGrade', models.IntegerField(verbose_name='Муковоз высший сорт, кг')),
                ('TransportSecondGrade', models.IntegerField(verbose_name='Муковоз второй сорт, кг')),
                ('Semolina', models.IntegerField(verbose_name='Манка, кг')),
                ('Comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_sfa_creator', to=settings.AUTH_USER_MODEL)),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m_sfa_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('m_sfa_list_view', 'УМС. Просмотр списка'), ('m_sfa_item_view', 'УМС. Просмотр записи'), ('m_sfa_item_add', 'УМС. Добавление записи'), ('m_sfa_item_edit', 'УМС. Редактирование записи')),
                'verbose_name_plural': 'Учет муки на складе (УМС)',
                'verbose_name': 'Смена ',
            },
        ),
        migrations.AlterModelOptions(
            name='mill_grain_waste_accounting',
            options={'permissions': (('m_gwa_list_view', 'УЗО. Просмотр списка'), ('m_gwa_item_view', 'УЗО. Просмотр записи'), ('m_gwa_item_add', 'УЗО. Добавление записи'), ('m_gwa_item_edit', 'УЗО. Редактирование записи')), 'verbose_name': 'Смена ', 'verbose_name_plural': 'Учёт зерноотходов на мельнице (УЗО)'},
        ),
        migrations.RenameField(
            model_name='mill_grain_waste_accounting',
            old_name='Bran2Varieties',
            new_name='BranSecondGrade',
        ),
        migrations.AddField(
            model_name='mill_grain_waste_accounting',
            name='Bran',
            field=models.IntegerField(default=0, verbose_name='Отруби, кг.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mill_grain_waste_accounting',
            name='Comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
    ]