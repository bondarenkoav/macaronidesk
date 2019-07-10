from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from dashboard.models import menu


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(menu, DraggableMPTTAdmin)
