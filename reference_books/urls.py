__author__ = 'ipman'

from reference_books.views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^clients/item/(?:id-(?P<id_item>\d+)/)?$', addget_rb_client, name='addget_client'),
    url(r'^clients/$', getlist_rb_clients, name='getlist_clients'),

    url(r'^posts/item/(?:id-(?P<id_item>\d+)/)?$', addget_rb_post, name='addget_post'),
    url(r'^posts/$', getlist_rb_posts, name='getlist_posts'),

    url(r'^products/item/(?:id-(?P<id_item>\d+)/)?$', addget_rb_product, name='addget_product'),
    url(r'^products/$', getlist_rb_products, name='getlist_products'),

    url(r'', rb_index, name='rb_dashboard'),
]