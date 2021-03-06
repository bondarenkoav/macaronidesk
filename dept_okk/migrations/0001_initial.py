# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 19:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reference_books', '0008_auto_20181205_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='okk_control_grain_moisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('note', models.CharField(max_length=50, verbose_name='Хруст (минеральная примесь)')),
                ('Moisture_excuse1', models.IntegerField(help_text='Указывается в %', verbose_name='Отлежка 1')),
                ('Moisture_excuse2', models.IntegerField(help_text='Указывается в %', verbose_name='Отлежка 2')),
                ('Moisture_excuse3', models.IntegerField(help_text='Указывается в %', verbose_name='Отлежка 3')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_cgm_creator', to=settings.AUTH_USER_MODEL)),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_cgm_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Замер ',
                'verbose_name_plural': 'Контроль увлажнения зерна на мельнице ',
            },
        ),
        migrations.CreateModel(
            name='okk_operational_quality_control_flour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('FlourGrade', models.CharField(choices=[('supreme', 'Высший сорт'), ('second', 'Второй сорт'), ('bran', 'Отруби')], max_length=50, verbose_name='Сорт муки')),
                ('BatchNumber', models.CharField(max_length=50, verbose_name='№ тонны')),
                ('Productivity', models.IntegerField(help_text='Указывается в кг/час', verbose_name='Производительность')),
                ('MoistureInfratek', models.IntegerField(help_text='Указывается в %', verbose_name='Влажность/Инфратек')),
                ('Residue', models.IntegerField(help_text='Указывается в %', verbose_name='Остаток')),
                ('Foramen', models.IntegerField(help_text='Указывается в %', verbose_name='Проход')),
                ('MetalImpurity', models.IntegerField(help_text='Указывается в мг/кг', verbose_name='Металлопримесь')),
                ('Inclusion_Black', models.CharField(max_length=50, verbose_name='Вкрапления черные')),
                ('Inclusion_Brown', models.CharField(max_length=50, verbose_name='Вкрапления коричневые')),
                ('Inclusion_Green', models.CharField(max_length=50, verbose_name='Вкрапления зеленые')),
                ('Inclusion_Extraneous', models.CharField(max_length=50, verbose_name='Посторонние включения')),
                ('Factor_a', models.CharField(max_length=50, verbose_name='Коэффициент a')),
                ('Factor_b', models.CharField(max_length=50, verbose_name='Коэффициент b')),
                ('Crunch', models.CharField(max_length=50, verbose_name='Хруст (минеральная примесь)')),
                ('Contamination', models.CharField(max_length=50, verbose_name='Зараженность/загрязненность')),
                ('AshContent', models.IntegerField(help_text='Указывается в %', verbose_name='Зольность')),
                ('Acidity', models.IntegerField(help_text='Указывается в %', verbose_name='Кислотность')),
                ('Gluten', models.IntegerField(help_text='Указывается в %', verbose_name='Клейковина отмытая вручную')),
                ('IDK', models.IntegerField(help_text='Указывается в усл.ед.', verbose_name='ИДК')),
                ('GlutenInfratek', models.IntegerField(help_text='Указывается в %', verbose_name='Клейковина/Инфратек')),
                ('Protein', models.IntegerField(help_text='Указывается в %', verbose_name='Белок')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_oqcf_creator', to=settings.AUTH_USER_MODEL)),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_oqcf_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Партия ',
                'verbose_name_plural': 'Оперативный качественный контроль муки на мельнице',
            },
        ),
        migrations.CreateModel(
            name='okk_operational_quality_control_semolina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('BatchNumber', models.CharField(max_length=50, verbose_name='№ тонны')),
                ('Productivity', models.IntegerField(help_text='Указывается в кг/час', verbose_name='Производительность')),
                ('Moisture', models.IntegerField(help_text='Указывается в %', verbose_name='Влажность')),
                ('Foramen', models.IntegerField(help_text='Указывается в %', verbose_name='Проход')),
                ('MetalImpurity', models.IntegerField(help_text='Указывается в мг/кг', verbose_name='Металлопримесь')),
                ('Inclusion_Black', models.CharField(max_length=50, verbose_name='Вкрапления черные')),
                ('Inclusion_Brown', models.CharField(max_length=50, verbose_name='Вкрапления коричневые')),
                ('Inclusion_Green', models.CharField(max_length=50, verbose_name='Вкрапления зеленые')),
                ('Inclusion_Extraneous', models.CharField(max_length=50, verbose_name='Посторонние включения')),
                ('Factor_a', models.CharField(max_length=50, verbose_name='Коэффициент a')),
                ('Factor_b', models.CharField(max_length=50, verbose_name='Коэффициент b')),
                ('Crunch', models.CharField(max_length=50, verbose_name='Хруст')),
                ('Contamination', models.CharField(max_length=50, verbose_name='Зараженность')),
                ('AshContent', models.IntegerField(help_text='Указывается в %', verbose_name='Зольность')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_oqcs_creator', to=settings.AUTH_USER_MODEL)),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_oqcs_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Замер ',
                'verbose_name_plural': 'Оперативный контроль качества манной муки',
            },
        ),
        migrations.CreateModel(
            name='okk_packproducts_quality_control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('BatchNumber', models.CharField(max_length=30, verbose_name='№ партии')),
                ('Moisture', models.IntegerField(help_text='Указывается в %', verbose_name='Влажность')),
                ('DeviationFromAverageLength', models.IntegerField(help_text='Указывается в %', verbose_name='Отклонение от средней длины')),
                ('Crumb', models.IntegerField(help_text='Указывается в %', verbose_name='Крошка')),
                ('Deformation', models.IntegerField(help_text='Указывается в %', verbose_name='Деформация')),
                ('Split', models.IntegerField(help_text='Указывается в %', verbose_name='Раскол')),
                ('Cut', models.CharField(max_length=100, verbose_name='Качество среза')),
                ('ImpregnationTrace', models.CharField(max_length=100, verbose_name='Наличие следов непромеса, вкрапления')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_pqc_creator', to=settings.AUTH_USER_MODEL)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.products', verbose_name='Вид макаронных изделий')),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_pqc_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Партия ',
                'verbose_name_plural': 'Контроль качества фасованной продукции ',
            },
        ),
        migrations.CreateModel(
            name='okk_wheat_quality_control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_word', models.DateField(verbose_name='Дата контроля')),
                ('Time_word', models.TimeField(verbose_name='Время контроля')),
                ('CarNumber', models.CharField(max_length=100, verbose_name='Гос.номер автомобиля')),
                ('LotWeight', models.DecimalField(decimal_places=3, help_text='Указывается в тоннах. Например: 20,456', max_digits=6, verbose_name='Масса партии')),
                ('Grain_Nature', models.IntegerField(help_text='Указывается в грамм/литр', verbose_name='Натура')),
                ('Grain_Moisture', models.IntegerField(help_text='Указывается в %', verbose_name='Влажность')),
                ('Grain_Vitreous', models.IntegerField(help_text='Указывается в %', verbose_name='Стекловидность')),
                ('Grain_Gluten', models.IntegerField(help_text='Указывается в %', verbose_name='Клейковина')),
                ('Grain_IDK', models.IntegerField(help_text='Указывается в усл.ед.', verbose_name='ИДК')),
                ('Grain_Protein', models.IntegerField(help_text='Указывается в %', verbose_name='Белок')),
                ('DustImpurity_OvsyugKukol', models.IntegerField(help_text='Указывается в %', verbose_name='Овсюг/Куколь')),
                ('DustImpurity_PolovaSeeds', models.IntegerField(help_text='Указывается в %', verbose_name='Полова/Семена')),
                ('DustImpurity_SprigsSeeds', models.IntegerField(help_text='Указывается в %', verbose_name='Веточки/Семечки')),
                ('DustImpurity_Fug', models.IntegerField(help_text='Указывается в %', verbose_name='Сор/Пыль')),
                ('DustImpurity_Minerals', models.IntegerField(help_text='Указывается в %', verbose_name='Минеральная примесь')),
                ('DustImpurity_Spoiled', models.IntegerField(help_text='Указывается в %', verbose_name='Испорченные')),
                ('GrainImpurity_Beaten', models.IntegerField(help_text='Указывается в %', verbose_name='Битое/Щуплое')),
                ('GrainImpurity_Eaten', models.IntegerField(help_text='Указывается в %', verbose_name='Изъеденное/Зеленое')),
                ('GrainImpurity_Rye', models.IntegerField(help_text='Указывается в %', verbose_name='Рожь/Поврежденное')),
                ('GrainImpurity_Barley', models.IntegerField(help_text='Указывается в %', verbose_name='Ячмень')),
                ('GrainImpurity_Sprouted', models.IntegerField(help_text='Указывается в %', verbose_name='Проросшее')),
                ('Defect_Small', models.IntegerField(help_text='Указывается в %', verbose_name='Мелкое')),
                ('Defect_Soft', models.IntegerField(help_text='Указывается в %', verbose_name='Мягкая')),
                ('Defect_Cracks', models.IntegerField(help_text='Указывается в %', verbose_name='С трещинами')),
                ('Defect_BlackGerm', models.IntegerField(help_text='Указывается в %', verbose_name='С черным зародышем')),
                ('DateTime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('DateTime_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('CerealCrop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.cereal_crop', verbose_name='Зерновая культура')),
                ('Create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_wqc_creator', to=settings.AUTH_USER_MODEL)),
                ('Provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.partner', verbose_name='Поставщик')),
                ('Update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okk_wqc_modifying', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Партия ',
                'verbose_name_plural': 'Входной контроль качества пшеницы ',
            },
        ),
    ]
