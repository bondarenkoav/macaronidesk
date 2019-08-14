# -*- coding: utf-8 -*-
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class constants(models.Model):
    name = models.CharField(u'Наименование', max_length=100)
    slug = models.SlugField(u'алиас')
    value = models.CharField(u'Значение', max_length=100)

    def __str__(self):  return self.name
    class Meta:
        verbose_name = u'Константа '
        verbose_name_plural = u'Список констант '


class area(MPTTModel):
    name    = models.CharField(u'Название', max_length=50)
    slug    = models.SlugField(u'Ключ категории')
    parent  = TreeForeignKey(u'self', blank=True, null=True, verbose_name="Родитель", related_name='child', db_index=True)

    def __str__(self): return self.name
    class Meta:
        verbose_name = u'Участок/Отдел '
        verbose_name_plural = u'Структура подразделений '
    class MPTTMeta:
        level_attr = 'mptt_level'


class posts(models.Model):
    name = models.CharField(u'Должность',max_length=100)
    #slug = models.SlugField(u'алиас')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(posts, self).save(*args, **kwargs)

    def __str__(self): return self.name
    class Meta:
        ordering = ['id']
        verbose_name = u'Должность '
        verbose_name_plural = u'Список должностей '


class coworker(models.Model):
    fullname = models.CharField(u'ФИО сотрудника', max_length=100)
    area     = models.ForeignKey(area, verbose_name=u'Подразделение')
    post     = models.ForeignKey(posts, verbose_name=u'Должность')
    working  = models.BooleanField(u'Действующий сотрудник', default=True, help_text=u'Если сотрудник уволен, снимите галочку')

    def __str__(self):  return self.fullname
    class Meta:
        ordering = ['fullname']
        verbose_name = u'Исполнитель/Сотрудник '
        verbose_name_plural = u'Список исполнителей '


class status(models.Model):
    name  = models.CharField(u'Состояние', max_length=100)
    slug  = models.SlugField(u'Ключ статуса', unique=True)
    color = models.CharField(u'Цвет строки', max_length=50)

    def __str__(self):  return self.name
    class Meta:
        verbose_name = u'Статус заявки '
        verbose_name_plural = u'Статусы заявок '

class status_task(models.Model):
    name  = models.CharField(u'Состояние', max_length=100)
    slug  = models.SlugField(u'Ключ статуса', unique=True)
    color = models.CharField(u'Цвет строки', max_length=50, blank=True, null=True)

    def __str__(self):  return self.name
    class Meta:
        verbose_name = u'Статус '
        verbose_name_plural = u'Статусы задач '


class BHM(models.Model):
    name  = models.CharField(u'Наименование', max_length=100)
    slug  = models.SlugField(u'Ключ статуса', unique=True)

    def __str__(self): return self.name
    class Meta:
        ordering = ['name']
        verbose_name = u'БХМ '
        verbose_name_plural = u'Установки БХМ '

class Sil(models.Model):
    name  = models.CharField(u'Наименование', max_length=100)
    slug  = models.SlugField(u'Ключ статуса', unique=True)

    def __str__(self): return self.name
    class Meta:
        ordering = ['name']
        verbose_name = u'Силос '
        verbose_name_plural = u'Установки силосные '


class typenotification_task(models.Model):
    name  = models.CharField(u'Состояние', max_length=100)
    slug  = models.SlugField(u'Ключ статуса', unique=True)
    color = models.CharField(u'Цвет строки', max_length=50, blank=True, null=True)

    def __str__(self):  return self.name
    class Meta:
        verbose_name = u'Тип '
        verbose_name_plural = u'Варианты уведомления '


class types_client(models.Model):    # Типы клиентов: ИП, Физлицо, Юрлицо
    short_name = models.CharField(u'Абревиатура',max_length=30)
    slug       = models.SlugField(u'Алиас',unique=True)
    full_name  = models.TextField(u'Подробное описание')

    def __str__(self):  return self.full_name
    class Meta:
        verbose_name = u'Тип контрагентов '
        verbose_name_plural = u'Типы контрагентов '


class partner(models.Model): # поставщик/покупатель
    type = models.ForeignKey(types_client, verbose_name=u'Тип поставщика')
    shortname = models.CharField(u'Краткое наименование', max_length=150)
    fullname = models.CharField(u'Полное наименование', max_length=300)
    inn = models.CharField(u'ИНН', max_length=15, blank=True)

    def __str__(self): return self.type.short_name + ' ' + self.shortname + ' (' + self.inn + ')'
    class Meta:
        ordering = ['shortname']
        verbose_name = u'Контрагент '
        verbose_name_plural = u'Контрагенты '


# Пшеница Ячмень Овес Рожь Просо Кукуруза Полба Гречиха Киноа
class cereal_crop(models.Model): # зерновые культуры
    name = models.CharField(u'Наименование', max_length=100)

    def __str__(self): return self.name
    class Meta:
        verbose_name = u'Культура '
        verbose_name_plural = u'Зерновые культуры '


class tare(models.Model): # виды тары
    name = models.CharField(u'Наименование', max_length=100)

    def __str__(self):  return self.name
    class Meta:
        verbose_name = u'вид '
        verbose_name_plural = u'Тара '


class products(models.Model): # макаронные изделия
    name = models.CharField(u'Наименование', max_length=255)

    def __str__(self):  return self.name
    class Meta:
        ordering = ['id']
        verbose_name = u'Вид '
        verbose_name_plural = u'Продукция '


class magnetic_installations(models.Model):
    name = models.CharField(u'Наименование', max_length=30)

    def __str__(self):  return u'Установка '+self.name
    class Meta:
        verbose_name = u'Установка '
        verbose_name_plural = u'Магнитные установки '


class fixed_assets(models.Model):
    area = models.ForeignKey(area, verbose_name=u'Подразделение (место установки)')
    name = models.CharField(u'Наименование', max_length=30)
    norm = models.IntegerField(u'Учтено, шт.')

    def __str__(self):  return self.area.name
    class Meta:
        verbose_name = u'Установка '
        verbose_name_plural = u'Основные средства '


class machine_production(models.Model):
    name = models.CharField(u'Наименование', max_length=100)
    slug = models.SlugField()

    def __str__(self): return self.name
    class Meta:
        ordering = ['id']
        verbose_name = u'Станок '
        verbose_name_plural = u'Станки для производства макарон '


class status_machine(models.Model):
    name = models.CharField(u'Наименование', max_length=100)
    slug = models.SlugField()
    class_b4_td = models.SlugField()

    def __str__(self):  return self.name
    class Meta:
        verbose_name = u'Состояние '
        verbose_name_plural = u'Состояния станков '


class City(models.Model):
    Name    = models.CharField(u'Город',max_length=100)
    slug    = models.SlugField(u'алиас')

    def __str__(self): return self.Name
    class Meta:
        ordering = ['Name']
        verbose_name = u'Город '
        verbose_name_plural = u'Список городов '


class Factory(models.Model):
    Name    = models.CharField(u'Наименование', max_length=100)
    City    = models.ForeignKey(City, verbose_name=u'Город')
    #slug    = models.SlugField(u'алиас', unique=True)
    Descript = models.TextField(u'Описание (специфика производства)', blank=True)

    def __str__(self): return self.Name
    class Meta:
        verbose_name = u'Фабрика/завод '
        verbose_name_plural = u'Список производств '