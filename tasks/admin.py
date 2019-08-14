from django.contrib import admin
from tasks.models import user_task


class UserTasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'DateTime_add', 'DateTime_update','status']
    filter = ['DateTime_add','Create_user','status']

admin.site.register(user_task, UserTasksAdmin)