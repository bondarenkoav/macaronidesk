# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import django_filters
from reference_books.models import coworker, machine_production, products, status_machine, Factory

LINE = (
    ('line_byuler1', u'Линия 1'),
    ('line_byuler2', u'Линия 2'),
)

LINE_GANG = (
    ('line_gang1', u'Смена 1'),
    ('line_gang2', u'Смена 2'),
)

class product_line_operator(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Line        = models.CharField(u'Линия', choices=LINE, max_length=30)
    Gang        = models.CharField(u'Смена', choices=LINE_GANG, max_length=30)
    Coworker    = models.ManyToManyField(coworker, verbose_name=u'Исполнители',
                                         help_text=u'Для указания нескольких исполнителей используйте клавишу Ctrl')
    Event       = models.TextField(u'Описание события')
    Action      = models.TextField(u'Описание работ')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='pc_lo_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='pc_lo_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang+' на линии '+self.Line
    class Meta:
        verbose_name = u'Запись событий '
        verbose_name_plural = u'Журнал оператора линий Бюлер (ЖОЛБ)'
        permissions = (
            ('p_lo_list_view', u'ЖОЛБ. Просмотр списка'),
            ('p_lo_item_view', u'ЖОЛБ. Просмотр записи'),
            ('p_lo_item_add', u'ЖОЛБ. Добавление записи'),
            ('p_lo_item_edit', u'ЖОЛБ. Редактирование записи'),
        )

class productlineoperator_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = product_line_operator
        fields = ['Date_word']


PACK_GANG = (
    ('line_gang1', u'Смена 1'),
    ('line_gang2', u'Смена 2'),
)

class product_packing_equipment_adjuster(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang        = models.CharField(u'Смена', choices=PACK_GANG, max_length=30)
    Coworker    = models.ManyToManyField(coworker, verbose_name=u'Исполнители',
                                         help_text=u'Для указания нескольких исполнителей используйте клавишу Ctrl')
    Event       = models.TextField(u'Описание события')
    Action      = models.TextField(u'Описание события')
    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='p_pea_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_pea_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Запись событий '
        verbose_name_plural = u'Журнал наладчика фасовочного оборудования (ЖНФО)'
        permissions = (
            ('p_pea_list_view', u'ЖНФО. Просмотр списка'),
            ('p_pea_item_view', u'ЖНФО. Просмотр записи'),
            ('p_pea_item_add', u'ЖНФО. Добавление записи'),
            ('p_pea_item_edit', u'ЖНФО. Редактирование записи'),
        )

class productpackingequipmentadjuster_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = product_packing_equipment_adjuster
        fields = ['Date_word']


MAINTENANCE_STAFF_GANG = (
    ('line_gang1', u'Смена 1'),
    ('line_gang2', u'Смена 2'),
)

class product_equipment_breakdown_repair(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang        = models.CharField(u'Смена', choices=MAINTENANCE_STAFF_GANG, max_length=30)
    Coworker    = models.ManyToManyField(coworker, verbose_name=u'Исполнители',
                                         help_text=u'Для указания нескольких исполнителей используйте клавишу Ctrl')
    Event       = models.TextField(u'Описание события')
    Action      = models.TextField(u'Описание события')
    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='p_ebr_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='p_ebr_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Запись событий '
        verbose_name_plural = u'Учет поломок и ремонта оборудования (УПРО)'
        permissions = (
            ('p_ebr_list_view', u'УПРО. Просмотр списка'),
            ('p_ebr_item_view', u'УПРО. Просмотр записи'),
            ('p_ebr_item_add', u'УПРО. Добавление записи'),
            ('p_ebr_item_edit', u'УПРО. Редактирование записи'),
        )

class productequipmentbreakdownrepair_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = product_equipment_breakdown_repair
        fields = ['Date_word']


STATUS_MACHINE = (
    ('repairs', u'Ремонт'),
    ('maintenance', u'ТО'),
    ('works', u'Работает'),
    ('lieby', u'Бездействует'),
)

TYPE_TASK = (
    ('tasks', u'Задание'),
    ('restriction', u'Ограничение'),
)

# Производственный план
class product_work_plan(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    type_task = models.CharField(u'Тип записи', choices=TYPE_TASK, max_length=100)
    equipement = models.ForeignKey(machine_production, verbose_name=u'Оборудование', blank=True, null=True)
    status = models.ForeignKey(status_machine, verbose_name=u'Состояние станка', blank=True, null=True)
    status_descript = models.TextField(u'Описание работ', blank=True, null=True)
    date_start = models.DateField(u'Дата начала', null=True,blank=True)
    date_end = models.DateField(u'Дата окончания', null=True, blank=True)
    product = models.ForeignKey(products, verbose_name=u'Продукция', blank=True, null=True)
    volume = models.DecimalField(u'Объём плана', decimal_places=2, max_digits=8, blank=True, null=True, help_text=u'в тоннах')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='p_wp_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='p_wp_modifying')

    def __str__(self): return self.type_task+': '+str(self.date_start)+' - '+str(self.date_end)
    class Meta:
        verbose_name = u'Событие '
        verbose_name_plural = u'Производственный план'
        permissions = (
            ('p_wp_list_view', u'ПрП. Просмотр списка'),
            ('p_wp_item_view', u'ПрП. Просмотр записи'),
            ('p_wp_item_add', u'ПрП. Добавление записи'),
            ('p_wp_item_edit', u'ПрП. Редактирование записи'),
        )

class productworkplan_filter(django_filters.FilterSet):

    class Meta:
        model = product_work_plan
        fields = []