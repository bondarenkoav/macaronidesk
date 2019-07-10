__author__ = 'ipman'

from django.conf.urls import url
from mill_complex.views import *


urlpatterns = [
    # Элеватор
    url(r'^elevatorgrainintake/item/(?:(?P<id_item>\d+)/)?$', addget_mill_elevatorgrainintake,
        name='addget_elevatorgrainintake'),
    url(r'^elevatorgrainintake/$', getlist_mill_elevatorgrainintake,
        name='getlist_elevatorgrainintake'),

    url(r'^elevatorgrainwasteaccounting/item/(?:(?P<id_item>\d+)/)?$', addget_mill_elevatorgrainwasteaccounting,
        name='addget_elevatorgrainwasteaccounting'),
    url(r'^elevatorgrainwasteaccounting/$', getlist_mill_elevatorgrainwasteaccounting,
        name='getlist_elevatorgrainwasteaccounting'),

    url(r'^elevatorshipmentwheattomill/item/(?:(?P<id_item>\d+)/)?$', addget_mill_elevatorshipmentwheattomill,
        name='addget_elevatorshipmentwheattomill'),
    url(r'^elevatorshipmentwheattomill/$', getlist_mill_elevatorshipmentwheattomill,
        name='getlist_elevatorshipmentwheattomill'),


    # Мельница
    url(r'^bagging/item/(?:id-(?P<id_item>\d+)/)?$', addget_mill_bagging,
        name='addget_bagging'),
    url(r'^bagging/$', getlist_mill_bagging,
        name='getlist_bagging'),

    url(r'^grainwasteaccounting/item/(?:id-(?P<id_item>\d+)/)?$', addget_mill_grainwasteaccounting,
        name='addget_grainwasteaccounting'),
    url(r'^grainwasteaccounting/$', getlist_mill_grainwasteaccounting,
        name='getlist_grainwasteaccounting'),

    url(r'^controlmagneticinstallations/item/(?:id-(?P<id_item>\d+)/)?$', addget_mill_controlmagneticinstallations,
        name='addget_controlmagneticinstallations'),
    url(r'^controlmagneticinstallations/$', getlist_mill_controlmagneticinstallations,
        name='getlist_controlmagneticinstallations'),

    url(r'^laboratorywork/item/(?:id-(?P<id_item>\d+)/)?$', addget_mill_laboratorywork,
        name='addget_laboratorywork'),
    url(r'^laboratorywork/$', getlist_mill_laboratorywork,
        name='getlist_laboratorywork'),

    url(r'^technological/item/(?:id-(?P<id_item>\d+)/)?$', addget_mill_technological,
        name='addget_technological'),
    url(r'^technological/$', getlist_mill_technological,
        name='getlist_technological'),

    url(r'^storageflouraccounting/item/(?:id-(?P<id_item>\d+)/)?$', addget_mill_storageflouraccounting,
        name='addget_storageflouraccounting'),
    url(r'^storageflouraccounting/$', getlist_mill_storageflouraccounting,
        name='getlist_storageflouraccounting'),

    url(r'', mill_index, name='mill_dashboard'),
]