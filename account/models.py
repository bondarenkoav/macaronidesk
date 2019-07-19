# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from reference_books.models import Factory


GENDER_CHOICES = (
    ('man',u'Мужской'),
    ('woman',u'Женский')
)

class Profile(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(u'Место нахождения', max_length=50, blank=True)
    birthday = models.DateField(u'Дата рождения', null=True, blank=True)
    phone    = models.CharField(u'Номер телефона', blank=True, max_length=10, help_text=u'Вводить номер в федеральном формате, без кода страны 8 или +7')
    gender   = models.CharField(u'Пол', choices=GENDER_CHOICES, max_length=50, blank=True)

    factory = models.ManyToManyField(Factory, related_name='factory_select', verbose_name=u'Производства (доступные)', help_text='Выбрать сервисные компании доступные пользователю')
    factory_default = models.ForeignKey(Factory, related_name='factory_default', verbose_name=u'Производство (по умолчанию)', null=True, blank=True)
    factory_current = models.ForeignKey(Factory, related_name='factory_current', verbose_name= u'Производство (текущая)', null=True, blank=True)

    def __str__(self):
        return self.user.last_name+' '+self.user.first_name

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
