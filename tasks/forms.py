from datetime import datetime
from django import forms
from django.contrib.auth.models import Group
from django.forms import DateInput, TimeInput, TimeField, DateField, ModelForm, CharField
from reference_books.models import status_task, typenotification_task

from tasks.models import user_task


class form_add_task(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(form_add_task, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)

        if instance and instance.id:
            if self.user != instance.author:
                self.fields['title'].required = False
                self.fields['title'].widget.attrs['disabled'] = 'disabled'
                self.fields['description'].required = False
                self.fields['description'].widget.attrs['disabled'] = 'disabled'
                self.fields['executors'].required = False
                self.fields['executors'].widget.attrs['disabled'] = 'disabled'
                self.fields['Date_limit'].required = False
                self.fields['Date_limit'].widget.attrs['disabled'] = 'disabled'
                self.fields['Time_limit'].required = False
                self.fields['Time_limit'].widget.attrs['disabled'] = 'disabled'
                self.fields['high_importance'].required = False
                self.fields['high_importance'].widget.attrs['disabled'] = 'disabled'
                self.fields['notification'].required = False
                self.fields['notification'].widget.attrs['disabled'] = 'disabled'
                self.fields['confirmation'].required = False
                self.fields['confirmation'].widget.attrs['disabled'] = 'disabled'
            else:
                if instance.status == status_task.objects.exclude(slug='complete'):
                    self.fields['notification'].required = False
                    self.fields['notification'].widget.attrs['disabled'] = 'disabled'
        else:
            self.fields['notification'].inintial = typenotification_task.objects.get(slug='system')
            self.fields['status'].initial = status_task.objects.get(slug='open')
            self.fields['status'].required = False
            self.fields['status'].widget.attrs['disabled'] = 'disabled'
            self.fields['work_desc'].required = False
            self.fields['work_desc'].widget.attrs['disabled'] = 'disabled'
            self.fields['notification'].required = False
            self.fields['notification'].widget.attrs['disabled'] = 'disabled'

        self.fields['read'].required = False
        self.fields['read'].widget.attrs['disabled'] = 'disabled'

    Date_limit = DateField(input_formats=('%Y-%m-%d',), initial=datetime.today(),
                           widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    Time_limit = TimeField(input_formats=('%H:%M',), initial=datetime.now(),
                           widget=TimeInput(format='%H:%M', attrs={'type': 'time'}))
    description = CharField(required=False, label='Описание задачи',
                            widget=forms.widgets.Textarea(attrs={'rows': 3}))
    work_desc = CharField(required=False, label='Описание выполнения',
                          widget=forms.widgets.Textarea(attrs={'rows': 3}))

    class Meta:
        model = user_task
        fields = ['title', 'description', 'executors', 'Date_limit', 'Time_limit',
                  'high_importance', 'notification', 'status', 'work_desc', 'read', 'confirmation']


