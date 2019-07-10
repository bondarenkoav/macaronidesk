from django.contrib import admin
from production_complex.models import product_line_operator, product_packing_equipment_adjuster, \
    product_equipment_breakdown_repair, product_work_plan


class admin_pc_lineoperator(admin.ModelAdmin):
    fields = ['DateTime','Line','Gang','Coworker','Event','Action']

class admin_pc_equipmentbreakdownrepair(admin.ModelAdmin):
    fields = ['DateTime','Gang','Coworker','Event','Action']

class admin_pc_packingequipmentadjuster(admin.ModelAdmin):
    fields = ['DateTime','Gang','Coworker','Event','Action']


admin.site.register(product_line_operator, admin_pc_lineoperator)
admin.site.register(product_packing_equipment_adjuster, admin_pc_packingequipmentadjuster)
admin.site.register(product_equipment_breakdown_repair, admin_pc_equipmentbreakdownrepair)
admin.site.register(product_work_plan)