from django.contrib.auth.models import User
from django.db import models
from reference_books.models import coworker, Factory, status_project


class project(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    Name = models.CharField(u'Наименование', max_length=100)
    Descript = models.TextField(u'Примечание', blank=True)
    Coworker = models.ForeignKey(coworker, verbose_name=u'Исполнители',
                                    help_text=u'Для указания нескольких исполнителей используйте клавишу Ctrl')
    Date_start = models.DateField(u'Дата начала')
    Date_end = models.DateField(u'Дата окнчания', null=True, blank=True)
    status = models.ForeignKey(status_project, verbose_name=u'Статус выполнения', default=1)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='project_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='project_modifying')

    def __str__(self):
        return u'Проект "' + self.Name + '"'
    class Meta:
        verbose_name = u'Проект '
        verbose_name_plural = u'Общие проекты'
        permissions = (
            ('projects_list_view', u'Проекты. Просмотр списка'),
            ('projects_item_view', u'Проекты. Просмотр записи'),
            ('projects_item_add', u'Проекты. Добавление записи'),
            ('projects_item_edit', u'Проекты. Редактирование записи'),
        )
