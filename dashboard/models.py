# -*- coding: utf-8 -*-
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class menu(MPTTModel):
    name    = models.CharField(u'Название', max_length=50)
    slug    = models.SlugField(u'Ключ категории')
    parent  = TreeForeignKey(u'self', blank=True, null=True, verbose_name="Родитель", related_name='child', db_index=True)
    icon    = models.CharField(u'Класс иконки bootstrap4', max_length=10, help_text="Допустим: search", blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'Ветка меню '
        verbose_name_plural = u'Дерево меню '
    class MPTTMeta:
        level_attr = 'mptt_level'
