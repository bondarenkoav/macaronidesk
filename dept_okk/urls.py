__author__ = 'ipman'

from django.conf.urls import url
from dept_okk.views import getlist_okk_wheatqualitycontrol, addget_okk_wheatqualitycontrol, \
    addget_okk_operationalqualitycontrolflour, getlist_okk_operationalqualitycontrolflour, \
    addget_okk_controlgrainmoisture, getlist_okk_controlgrainmoisture, getlist_okk_packproductsqualitycontrol, \
    addget_okk_packproductsqualitycontrol, getlist_okk_operationalqualitycontrolsemolina, \
    addget_okk_operationalqualitycontrolsemolina, okk_index


urlpatterns = [
    url(r'^wheatqualitycontrol/item/(?:id-(?P<id_item>\d+)/)?$', addget_okk_wheatqualitycontrol,
        name='addget_wheatqualitycontrol'),
    url(r'^wheatqualitycontrol/$', getlist_okk_wheatqualitycontrol,
        name='getlist_wheatqualitycontrol'),

    url(r'^operationalqualitycontrolflour/item/(?:id-(?P<id_item>\d+)/)?$', addget_okk_operationalqualitycontrolflour,
        name='addget_operationalqualitycontrolflour'),
    url(r'^operationalqualitycontrolflour/$', getlist_okk_operationalqualitycontrolflour,
        name='getlist_operationalqualitycontrolflour'),

    url(r'^controlgrainmoisture/item/(?:id-(?P<id_item>\d+)/)?$', addget_okk_controlgrainmoisture,
        name='addget_controlgrainmoisture'),
    url(r'^controlgrainmoisture/$', getlist_okk_controlgrainmoisture,
        name='getlist_controlgrainmoisture'),

    url(r'^operationalqualitycontrolsemolina/item/(?:id-(?P<id_item>\d+)/)?$', addget_okk_operationalqualitycontrolsemolina,
        name='addget_operationalqualitycontrolsemolina'),
    url(r'^operationalqualitycontrolsemolina/$', getlist_okk_operationalqualitycontrolsemolina,
        name='getlist_operationalqualitycontrolsemolina'),

    url(r'^packproductsqualitycontrol/item/(?:id-(?P<id_item>\d+)/)?$', addget_okk_packproductsqualitycontrol,
        name='addget_packproductsqualitycontrol'),
    url(r'^packproductsqualitycontrol/$', getlist_okk_packproductsqualitycontrol,
        name='getlist_packproductsqualitycontrol'),

    url(r'^', okk_index, name='okk_dashboard'),
]