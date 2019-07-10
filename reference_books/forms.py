__author__ = 'ipman'

from django.forms import ModelForm
from reference_books.models import partner, posts, products


class form_client(ModelForm):
    class Meta:
        model = partner
        fields = '__all__'


class form_post(ModelForm):
    class Meta:
        model = posts
        fields = '__all__'


class form_product(ModelForm):
    class Meta:
        model = products
        fields = '__all__'