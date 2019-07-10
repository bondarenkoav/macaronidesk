from django.contrib import admin
from tasks.models import user_task


# class UserTasksAdmin(admin.ModelAdmin):
#     list_display = ['title', 'responsible', 'limitation', 'DateTime_add', 'DateTime_update','done']
#     filter = ['DateTime_add','Create_user','responsible','done']

admin.site.register(user_task) #, UserTasksAdmin)