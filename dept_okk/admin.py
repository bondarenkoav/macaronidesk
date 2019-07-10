#-*- coding: utf-8 -*-
from django.contrib import admin
from dept_okk.models import okk_operational_quality_control_semolina, okk_wheat_quality_control, \
    okk_operational_quality_control_flour, okk_control_grain_moisture, okk_packproducts_quality_control

class admin_okk_wheatqualitycontrol(admin.ModelAdmin):
    fieldsets = [
        (u'Данные о партии', {'fields':  ['Date_word', 'Time_word', 'Provider', 'CarNumber', 'CerealCrop', 'LotWeight']}),
        (u'Основные параметры зерна', {'fields':  ['Grain_Nature', 'Grain_Moisture', 'Grain_Vitreous', 'Grain_Gluten', 'Grain_IDK', 'Grain_Protein']}),
        (u'Сорная примесь', {'fields':  ['DustImpurity_OvsyugKukol', 'DustImpurity_PolovaSeeds', 'DustImpurity_SprigsSeeds', 'DustImpurity_Fug', 'DustImpurity_Minerals', 'DustImpurity_Spoiled']}),
        (u'Зерновая примесь', {'fields':  ['GrainImpurity_Beaten', 'GrainImpurity_Eaten', 'GrainImpurity_Rye', 'GrainImpurity_Barley', 'GrainImpurity_Sprouted']}),
        (u'Дефекты зерна', {'fields': ['Defect_Small', 'Defect_Soft', 'Defect_Cracks', 'Defect_BlackGerm']})
    ]

class admin_okk_operationalqualitycontrolflour(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word', 'Time_word','FlourGrade','BatchNumber','Productivity','MoistureInfratek']}),
        (None, {'fields':  ['Residue', 'Foramen', 'MetalImpurity']}),
        (u'Вкрапления', {'fields':  ['Inclusion_Black', 'Inclusion_Brown', 'Inclusion_Green', 'Inclusion_Extraneous']}),
        (u'Коэффициенты', {'fields':  ['Factor_a', 'Factor_b']}),
        (None, {'fields':  ['Crunch', 'Contamination', 'AshContent', 'Acidity', 'Gluten', 'IDK', 'GlutenInfratek', 'Protein']})
    ]

class admin_okk_controlgrainmoisture(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word', 'Time_word']}),
        (u'Отлёжка', {'fields':  ['Moisture_excuse1', 'Moisture_excuse2', 'Moisture_excuse3']})
    ]

class admin_okk_operationalqualitycontrolsemolina(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word', 'Time_word','BatchNumber', 'Productivity']}),
        (None, {'fields':  ['Moisture', 'Foramen', 'MetalImpurity']}),
        (u'Вкрапления', {'fields':  ['Inclusion_Black', 'Inclusion_Brown', 'Inclusion_Green', 'Inclusion_Extraneous']}),
        (u'Коэффициенты', {'fields':  ['Factor_a', 'Factor_b']}),
        (None, {'fields':  ['Crunch', 'Contamination', 'AshContent']})
    ]

class admin_okk_packproductsqualitycontrol(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word', 'Time_word', 'Product', 'BatchNumber']}),
        (None, {'fields':  ['Moisture', 'DeviationFromAverageLength', 'Crumb', 'Deformation', 'Split', 'Cut', 'ImpregnationTrace']})
    ]

admin.site.register(okk_wheat_quality_control, admin_okk_wheatqualitycontrol)
admin.site.register(okk_operational_quality_control_flour, admin_okk_operationalqualitycontrolflour)
admin.site.register(okk_control_grain_moisture, admin_okk_controlgrainmoisture)
admin.site.register(okk_operational_quality_control_semolina, admin_okk_operationalqualitycontrolsemolina)
admin.site.register(okk_packproducts_quality_control, admin_okk_packproductsqualitycontrol)
