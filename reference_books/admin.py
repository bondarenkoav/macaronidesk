from django.contrib import admin
from reference_books.models import posts, coworker, status, partner, products, status_task, typenotification_task, BHM, \
    Factory, City

class StatusTasksAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

admin.site.register(posts)
admin.site.register(coworker)
admin.site.register(partner)
admin.site.register(status)
admin.site.register(products)
admin.site.register(status_task, StatusTasksAdmin)
admin.site.register(typenotification_task)
admin.site.register(BHM)
admin.site.register(City)
admin.site.register(Factory)