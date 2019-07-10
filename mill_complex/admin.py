# -*- coding: utf-8 -*-
from django.contrib import admin
from mill_complex.models import elevator_shipment_wheat_to_mill, mill_bagging, mill_grain_waste_accounting, \
    mill_control_magnetic_installations, mill_laboratory_work


class admin_mill_elevatorshipmentwheattomill(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word','Time_word']}),
        (u'Силос', {'fields':  ['Sil_1','Sil_2','Sil_3']}),
        (u'Измерения', {'fields':  ['Moisture','Nature','Gluten','Vitreous','Yellowish']}),
    ]

class admin_mill_bagging(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word','Time_word','Gang']}),
        (u'Получено, мешков', {'fields':  ['ReceivedBags_flour','ReceivedBags_zo','ReceivedBags_zelen']}),
        (u'Сдано, мешков', {'fields':  ['HandedOverBags_flour','HandedOverBags_zo','HandedOverBags_zelen']})
    ]

class admin_mill_grainwasteaccounting(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word','Time_word', 'Gang']}),
        (u'Исполнители', {'fields': ['Supervisor','Assistant',]}),
        (u'Пыль', {'fields':  ['KnockedOut','Dust']})
    ]

class admin_mill_controlmagneticinstallations(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word','Time_word','Verifier']}),
        (u'Результат проверки', {'fields':  ['CheckPassed', 'CheckFailed']}),
    ]

class admin_mill_laboratorywork(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['Date_word','Time_word', 'Verifier']}),
        (u'Отлёжка', {'fields':  ['Postponing_One','Postponing_Two','Postponing_Three']}),
        (u'Сорта', {'fields':  ['Grade_Top','Grade_Second']}),
        (u'Остаток', {'fields':  ['SieveResidue125','SieveResidue245']}),
        (u'Вкрапления', {'fields':  ['Inclusion_Black','Inclusion_Brown']}),
        (None, {'fields':  ['BAKBHM']})
    ]

admin.site.register(elevator_shipment_wheat_to_mill, admin_mill_elevatorshipmentwheattomill)
admin.site.register(mill_bagging, admin_mill_bagging)
admin.site.register(mill_grain_waste_accounting, admin_mill_grainwasteaccounting)
admin.site.register(mill_control_magnetic_installations, admin_mill_controlmagneticinstallations)
admin.site.register(mill_laboratory_work, admin_mill_laboratorywork)