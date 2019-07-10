# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from account.models import Profile

__author__ = 'ipman'

class login_form(forms.Form):
    username = forms.CharField(label=u'Логин')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(login_form, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None


class select_current_factory_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.factory = kwargs.pop('factory', None)
        super(select_current_factory_form, self).__init__(*args, **kwargs)

        self.fields['factory'].widget=forms.Select(attrs={'class':'selector'})
        self.fields['factory'].queryset = Profile.objects.get(user=self.user).factory.all()
        self.fields['factory'].initial = self.factory

    class Meta:
        model = Profile
        fields = ['factory']