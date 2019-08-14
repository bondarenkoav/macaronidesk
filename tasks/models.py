# -*- coding: utf-8 -*-
import django_filters
from django.contrib.auth.models import User, Group
from django.db import models
from account.models import Profile
from reference_books.models import status_task, typenotification_task, Factory


class user_task(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    title           = models.CharField(u'Заголовок задачи', max_length=100)
    description     = models.TextField(u'Описание задачи')
    author          = models.ForeignKey(User, verbose_name=u'Назначающий', related_name='author')
    executors       = models.ForeignKey(Group, verbose_name=u'Группа исполнителей', related_name='groups')
    Date_limit      = models.DateField(u'Дата исполнения')
    Time_limit      = models.TimeField(u'Время исполнения')
    high_importance = models.BooleanField(u'Высокая важность', default=False)
    notification    = models.ForeignKey(typenotification_task, verbose_name=u'Способ уведомления о статусе заявки')
    status          = models.ForeignKey(status_task, verbose_name=u'Статус выполнения')
    work_desc       = models.TextField(u'Описание выполнения', blank=True, null=True)
    read            = models.BooleanField(u'Прочтено', default=False)
    confirmation    = models.BooleanField(u'Подтверждение', default=False)

    Create_user     = models.ForeignKey(User, verbose_name=u'Создал', related_name='create_user')
    Update_user     = models.ForeignKey(User, verbose_name=u'Обновил', related_name='update_user', blank=True, null=True)
    DateTime_add    = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update = models.DateTimeField(u'Дата и время обновления', auto_now=True)

    def __str__(self):  return self.title
    class Meta:
        verbose_name = u'Задача '
        verbose_name_plural = u'Список задач '
        permissions = (
            ('task_list_view', u'Задачи. Просмотр списка'),
            ('task_item_view', u'Задачи. Просмотр записи'),
            ('task_item_add', u'Задачи. Добавление записи'),
            ('task_item_edit', u'Задачи. Редактирование записи'),
        )

class usertask_filter(django_filters.FilterSet):
    author      = django_filters.ModelChoiceFilter(queryset=Profile.objects.order_by('user__last_name'))
    executors   = django_filters.ModelChoiceFilter(queryset=Group.objects.order_by('name'))
    status      = django_filters.ModelChoiceFilter(queryset=status_task.objects.
                                                   exclude(slug__in=['confirmation','control','canceled']).
                                                   order_by('id'))
    class Meta:
        model = user_task
        fields = ['status','author','executors']