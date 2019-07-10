from django import forms
from account.models import Profile

__author__ = 'ipman'


class change_cur_factory_form(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(change_cur_factory_form, self).__init__(*args, **kwargs)
        profile = Profile.objects.get(user=self.user)

        self.fields['cur_factory'].queryset = profile.factory
        if profile.factory_current:
            self.fields['cur_factory'].initial = profile.factory_current
        elif profile.factory_default:
            self.fields['cur_factory'].initial = profile.factory_default
        else:
            self.fields['cur_factory'].initial = profile.factory.all().first()

    cur_factory = forms.ModelChoiceField(label=u'Производство', queryset=Profile.objects.values('factory').all(),
                                         initial=Profile.factory_current,
                                         widget=forms.Select(attrs={'class':'change_factory_selectfield'}))