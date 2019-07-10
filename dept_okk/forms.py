# -*- coding: utf-8 -*-
__author__ = 'ipman'

from datetime import datetime
from django.forms import ModelForm, DateField, TimeField, DateInput, TimeInput
from dept_okk.models import okk_wheat_quality_control, okk_operational_quality_control_flour, \
    okk_operational_quality_control_semolina, okk_control_grain_moisture, okk_packproducts_quality_control


class form_okk_wheatqualitycontrol(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = okk_wheat_quality_control
        fields = ['Date_word', 'Time_word', 'Provider', 'CarNumber', 'CerealCrop', 'LotWeight',
                  'Grain_Nature', 'Grain_Moisture', 'Grain_Vitreous', 'Grain_Gluten', 'Grain_IDK', 'Grain_Protein',
                  'DustImpurity_OvsyugKukol', 'DustImpurity_PolovaSeeds', 'DustImpurity_SprigsSeeds', 'DustImpurity_Fug', 'DustImpurity_Minerals', 'DustImpurity_Spoiled',
                  'GrainImpurity_Beaten', 'GrainImpurity_Eaten', 'GrainImpurity_Rye', 'GrainImpurity_Barley', 'GrainImpurity_Sprouted',
                  'Defect_Small', 'Defect_Soft', 'Defect_Cracks', 'Defect_BlackGerm']


class form_okk_operationalqualitycontrolflour(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = okk_operational_quality_control_flour
        fields = ['Date_word', 'Time_word', 'FlourGrade','BatchNumber','Productivity','MoistureInfratek',
                  'Residue', 'Foramen', 'MetalImpurity',
                  'Inclusion_Black', 'Inclusion_Brown', 'Inclusion_Green', 'Inclusion_Extraneous',
                  'Factor_a', 'Factor_b',
                  'Crunch', 'Contamination', 'AshContent', 'Acidity', 'Gluten', 'IDK', 'GlutenInfratek', 'Protein']


class form_okk_controlgrainmoisture(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = okk_control_grain_moisture
        fields = ['Date_word', 'Time_word', 'Moisture_excuse1', 'Moisture_excuse2', 'Moisture_excuse3']


class form_okk_operationalqualitycontrolsemolina(ModelForm):
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = okk_operational_quality_control_semolina
        fields = ['Date_word', 'Time_word', 'BatchNumber',
                  'Moisture', 'Foramen', 'MetalImpurity',
                  'Inclusion_Black', 'Inclusion_Brown', 'Inclusion_Green', 'Inclusion_Extraneous',
                  'Factor_a', 'Factor_b',
                  'Crunch', 'Contamination', 'AshContent']


class form_okk_packproductsqualitycontrol(ModelForm):  # контроль качества фасованной продукции
    Date_word = DateField(label=u'Дата ', input_formats=('%Y-%m-%d',), initial=datetime.today(),
                          widget=DateInput(format='%Y-%m-%d', attrs={'type':'date'}))
    Time_word = TimeField(label=u'Время ', input_formats=('%H:%M',), initial=datetime.now(),
                          widget=TimeInput(format='%H:%M', attrs={'type':'time'}))
    class Meta:
        model = okk_packproducts_quality_control
        fields = ['Date_word', 'Time_word', 'Product', 'BatchNumber',
                  'Moisture', 'DeviationFromAverageLength', 'Crumb', 'Deformation', 'Split', 'Cut', 'ImpregnationTrace']
