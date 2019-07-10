# -*- coding: utf-8 -*-
__author__ = 'ipman'

from datetime import datetime
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField, TimeField, DateInput, TimeInput, Form, ChoiceField
from production_complex.models import product_line_operator, product_packing_equipment_adjuster, \
    product_equipment_breakdown_repair, product_work_plan



class form_pc_lineoperator(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = product_line_operator
        fields = ['Date_word','Time_word','Line','Gang','Coworker','Event','Action']


class form_pc_equipmentbreakdownrepair(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = product_packing_equipment_adjuster
        fields = ['Date_word','Time_word','Gang','Coworker','Event','Action']


class form_pc_packingequipmentadjuster(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = product_equipment_breakdown_repair
        fields = ['Date_word','Time_word','Gang','Coworker','Event','Action']



class form_workplan(Form):
    choice_year = [(r,r) for r in range(2018, datetime.today().year+1)]
    choice_month = ((1,u'январь'),(2,u'февраль'),(3,u'март'),
                    (4,u'апрель'),(5,u'май'),(6,u'июнь'),
                    (7,u'июль'),(8,u'август'),(9,u'сентябрь'),
                    (10,u'октябрь'),(11,u'ноябрь'),(12,u'декабрь'))
    month_plan = ChoiceField(label="Месяц", choices=choice_month, initial=datetime.now().month)
    year_plan = ChoiceField(label="Год", choices=choice_year, initial=datetime.now().year)


class form_add_workplan(ModelForm):
    date_start = DateField(label=u'Дата', input_formats=('%Y-%m-%d',),
                           widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    class Meta:
        model = product_work_plan
        fields = ['equipement','date_start','product','volume']

    def clean(self):
        cleaned_data = super(form_add_workplan, self).clean()
        equipement = cleaned_data.get('equipement')
        date_task = cleaned_data['date_start']

        if not self.errors:
            restriction = product_work_plan.objects.\
                filter(type_task='restriction', equipement=equipement,
                       date_start__lte=date_task, date_end__gt=date_task)
            if restriction:
                raise ValidationError(u'Выберите другую дату задания')

        return cleaned_data


class form_add_restriction(ModelForm):
    date_start = DateField(label=u'Начало', input_formats=('%Y-%m-%d',),
                      widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    date_end = DateField(required=False, label=u'Конец', input_formats=('%Y-%m-%d',),
                    widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
                    help_text=u'Не обязательный параметр')
    class Meta:
        model = product_work_plan
        fields = ['equipement','status','status_descript','date_start','date_end']