# -*- coding: utf-8 -*-
from django.contrib import admin
from account.models import Profile, GroupProfile
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = u'Профиль'
    verbose_name_plural = u'Профиль'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class ProfileGroupInline(admin.StackedInline):
    model = GroupProfile
    can_delete = False
    verbose_name = u'Дополнительные поле'
    verbose_name_plural = u'Дополнительные поля'
    fk_name = 'group'

class CustomGroupAdmin(GroupAdmin):
    inlines = (ProfileGroupInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomGroupAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)