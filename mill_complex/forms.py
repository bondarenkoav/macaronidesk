# -*- coding: utf-8 -*-
__author__ = 'ipman'

import calendar
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, date
from django.forms import ModelForm, TimeField, DateField, TimeInput, DateInput, CharField, widgets, Form
from mill_complex.models import elevator_shipment_wheat_to_mill, mill_bagging, mill_grain_waste_accounting, \
mill_control_magnetic_installations, mill_laboratory_work, mill_technological, mill_technological_child_bhm, \
    elevator_shipment_wheat_to_mill_child_sil, elevator_grain_intake, mill_storage_flour_accounting, \
    elevator_grain_waste_accounting

# ---------------------------------------------------------------------------------------------------------
# -------------------- Э Л Е В А Т О Р --------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class form_mill_elevatorgrainintake(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = elevator_grain_intake
        fields = ['Date_word','Time_word','CarModel','CarNumber','Provider',
                  'CerealCrop','WeightGross','WeightTare','WeightNet','WeightActual','WeightCredit',
                  'Comment']


class form_mill_elevatorgrainwasteaccounting(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = elevator_grain_waste_accounting
        fields = ['Date_word','Time_word',
                  'GrainWaste','GrainWasteTopGrade','GrainWasteSecondGrade',
                  'Comment']


class form_mill_elevatorshipmentwheattomill(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = elevator_shipment_wheat_to_mill
        fields = ['Date_word','Time_word',
                  'Moisture','Nature','Gluten','Vitreous','Yellowish']

class form_mill_elevatorshipmentwheattomill_sil(ModelForm):
    class Meta:
        model = elevator_shipment_wheat_to_mill_child_sil
        fields = ['sil_num','grain','party']


# ---------------------------------------------------------------------------------------------------------
# -------------------- М Е Л Ь Н И Ц А --------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class form_mill_bagging(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = mill_bagging
        fields = ['Date_word','Time_word','Gang',
                  'ReceivedBags_flour','ReceivedBags_zo','ReceivedBags_zelen']


class form_mill_grainwasteaccounting(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = mill_grain_waste_accounting
        fields = ['Date_word','Time_word','Gang',
                  'GrainWaste','Bran','BranSecondGrade',
                  'Comment']


class form_mill_controlmagneticinstallations(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = mill_control_magnetic_installations
        fields = ['Date_word','Time_word','Gang',
                  'CheckPassed','CheckFailed']


class form_mill_laboratorywork(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = mill_laboratory_work
        fields = ['Date_word','Time_word','Gang',
                  'Postponing_One','Postponing_Two','Postponing_Three','Grade_Top','Grade_Second',
                  'Remainder_TopGrade','Passage_TopGrade','Yellowish_TopGrade','MetalImpurity_TopGrade','Crunch_TopGrade',
                  'GrainBlack','GrainBraun','GrainGreen','GrainWhite',
                  'Remainder_GradeSecond','Passage_GradeSecond',
                  'Bran_Nature']


class form_mill_technological(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    Description_work = CharField(required=False, label='Описание работы',
                                      widget=widgets.Textarea(attrs={'rows':3}))
    class Meta:
        model = mill_technological
        fields = ['Date_word', 'Time_word', 'Gang',
                  'Prod_Semolina','Prod_TopGrade_enum','Prod_SecondGrade_enum','Prod_Bran_enum','Prod_GrainWaste','Prod_Bran2Varieties',
                  'KnockedOut_TopGrade_start','KnockedOut_TopGrade_stop','KnockedOut_SecondGrade','KnockedOut_Semolina','Trans_Workshop',
                  'Description_work']

class form_mill_technological_bhm(ModelForm):
    class Meta:
        model = mill_technological_child_bhm
        fields = ['bhm_num','grain']


class form_mill_storageflouraccounting(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = mill_storage_flour_accounting
        fields = ['Date_word', 'Time_word',
                  'TopGrade','SecondGrade','TransportTopGrade','TransportSecondGrade','Semolina',
                  'Comment']

# ---------------------------------------------------------------------------------------------------------
# ------------------------ О Т Ч Е Т Ы --------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class form_report_mill_daily(Form):
    filter_date = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',),
                            initial=datetime.today() - timedelta(days=1),
                            widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    # def clean(self):
    #     cleaned_data = super(form_report_mill_daily, self).clean()
    #     filter_date = cleaned_data['filter_date']
    #
    #     if not self.errors:
    #         if filter_date > datetime.today():
    #             raise ValidationError(u'Данных за введенную дату быть не может')
    #
    #     return cleaned_data


class form_report_mill_grainwasteaccounting(Form):
    filter_start_date = DateField(required=True, label=u'Дата ', input_formats=('%Y-%m-%d',),
                                  initial=date(datetime.today().year, datetime.today().month, 1),
                                  widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    filter_end_date = DateField(required=True, label=u'Дата ', input_formats=('%Y-%m-%d',),
                                initial=date(datetime.today().year, datetime.today().month,
                                             calendar.monthrange(datetime.today().year, datetime.today().month)[1]),
                                widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))


class form_report_mill_grainconsumption(Form):
    filter_start_date = DateField(required=True, label=u'Дата ', input_formats=('%Y-%m-%d',),
                                  initial=date(datetime.today().year, datetime.today().month, 1),
                                  widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    filter_end_date = DateField(required=True, label=u'Дата ', input_formats=('%Y-%m-%d',),
                                initial=date(datetime.today().year, datetime.today().month,
                                             calendar.monthrange(datetime.today().year, datetime.today().month)[1]),
                                widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))