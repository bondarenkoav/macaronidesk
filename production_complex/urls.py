__author__ = 'ipman'

from django.conf.urls import url
from production_complex.views import addget_pc_productlineoperator, getlist_pc_productlineoperator, \
    addget_pc_packingequipmentadjuster, \
    getlist_pc_packingequipmentadjuster, addget_pc_equipmentbreakdownrepair, getlist_pc_equipmentbreakdownrepair, \
    pc_index, work_plan, add_work_plan, add_work_restriction

urlpatterns = [
    url(r'^productlineoperator/item/(?:id-(?P<id_item>\d+)/)?$', addget_pc_productlineoperator,
        name='addget_lineoperator'),
    url(r'^productlineoperator/$', getlist_pc_productlineoperator,
        name='getlist_lineoperator'),

    url(r'^packingequipmentadjuster/item/(?:id-(?P<id_item>\d+)/)?$', addget_pc_packingequipmentadjuster,
        name='addget_packingequipmentadjuster'),
    url(r'^packingequipmentadjuster/$', getlist_pc_packingequipmentadjuster,
        name='getlist_packingequipmentadjuster'),

    url(r'^equipmentbreakdownrepair/item/(?:id-(?P<id_item>\d+)/)?$', addget_pc_equipmentbreakdownrepair,
        name='addget_equipmentbreakdownrepair'),
    url(r'^equipmentbreakdownrepair/$', getlist_pc_equipmentbreakdownrepair,
        name='getlist_equipmentbreakdownrepair'),

    url(r'work_plan/add_restriction/$', add_work_restriction, name='add_work_restriction'),
    url(r'work_plan/add_plan/$', add_work_plan, name='add_work_plan'),
    url(r'work_plan/$', work_plan, name='work_plan'),
    url(r'^', pc_index, name='pc_dashboard'),
]