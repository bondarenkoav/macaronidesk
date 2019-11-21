__author__ = 'ipman'

from django.db.models import Sum, IntegerField, FloatField
from mill_complex.models import mill_technological, mill_technological_child_bhm, \
    elevator_shipment_wheat_to_mill_child_sil, elevator_shipment_wheat_to_mill, elevator_grain_waste_accounting, \
    mill_grain_waste_accounting, mill_storage_flour_accounting, elevator_grain_intake
from django import template

register = template.Library()

@register.filter
def getname_gang(slug):
    if slug == 'day_shift':
        return 'дневная'
    if slug == 'night_shift':
        return 'ночная'


@register.filter
def get_bhm(parent_id, bhm_id):
    return mill_technological_child_bhm.objects.get(parent_table=parent_id, bhm_num=bhm_id).grain

@register.filter
def get_sil(parent_id, sil_id):
    return elevator_shipment_wheat_to_mill_child_sil.objects.get(parent_table=parent_id, sil_num=sil_id).grain


@register.inclusion_tag('mill_complex/templatetags/mill_grainconsumption_tags.html')
def get_grainconsumption_tags(date):
    insilos = elevator_shipment_wheat_to_mill_child_sil.objects.\
        filter(parent_table__in=elevator_shipment_wheat_to_mill.objects.filter(Date_word=date)).\
        aggregate(ct=Sum('grain', output_field=FloatField()))
    insilos = float(0 if insilos['ct'] is None else insilos['ct'])

    intake = elevator_grain_intake.objects.\
        filter(Date_word=date).\
        aggregate(ct=Sum('WeightCredit', output_field=FloatField()))
    intake = float(0 if intake['ct'] is None else intake['ct'])

    residue = elevator_shipment_wheat_to_mill_child_sil.objects.\
        filter(parent_table__in=elevator_shipment_wheat_to_mill.objects.filter(Date_word__gt=date)).\
        order_by('DateTime_add').aggregate(ct=Sum('grain', output_field=FloatField()))
    residue = float(0 if residue['ct'] is None else residue['ct'])

    consumption = (insilos + intake) - residue

    return {
        'insilos': insilos,
        'intake': intake,
        'residue': residue,
        'consumption': consumption,
    }


@register.inclusion_tag('mill_complex/templatetags/mill_grainwasteaccounting_egwa_tags.html')
def get_elevator_grainwaste(date):
    mill_egwa = elevator_grain_waste_accounting.objects.filter(Date_word=date)

    mill_egwa_grainwaste = mill_egwa.aggregate(ct=Sum('GrainWaste', output_field=IntegerField()))
    mill_egwa_grainwaste = int(0 if mill_egwa_grainwaste['ct'] is None else mill_egwa_grainwaste['ct'])

    mill_egwa_grainwaste_firstgrade = mill_egwa.aggregate(ct=Sum('GrainWasteTopGrade', output_field=IntegerField()))
    mill_egwa_grainwaste_firstgrade = int(0 if mill_egwa_grainwaste_firstgrade['ct'] is None else mill_egwa_grainwaste_firstgrade['ct'])

    mill_egwa_grainwaste_secondgrade = mill_egwa.aggregate(ct=Sum('GrainWasteSecondGrade', output_field=IntegerField()))
    mill_egwa_grainwaste_secondgrade = int(0 if mill_egwa_grainwaste_secondgrade['ct'] is None else mill_egwa_grainwaste_secondgrade['ct'])

    return {'mill_egwa_grainwaste':mill_egwa_grainwaste,
            'mill_egwa_grainwaste_firstgrade': mill_egwa_grainwaste_firstgrade,
            'mill_egwa_grainwaste_secondgrade': mill_egwa_grainwaste_secondgrade}


@register.inclusion_tag('mill_complex/templatetags/mill_grainwasteaccounting_gwa_tags.html')
def get_mill_grainwaste(date):
    mill_gwa = mill_grain_waste_accounting.objects.filter(Date_word=date)

    mill_gwa_bran = mill_gwa.aggregate(ct=Sum('Bran', output_field=IntegerField()))
    mill_gwa_bran = int(0 if mill_gwa_bran['ct'] is None else mill_gwa_bran['ct'])

    mill_gwa_secondbran = mill_gwa.aggregate(ct=Sum('BranSecondGrade', output_field=IntegerField()))
    mill_gwa_secondbran = int(0 if mill_gwa_secondbran['ct'] is None else mill_gwa_secondbran['ct'])

    return {'mill_gwa_bran': mill_gwa_bran,
            'mill_gwa_secondbran': mill_gwa_secondbran}


@register.inclusion_tag('mill_complex/templatetags/mill_grainwasteaccounting_gwa_tags.html')
def get_sold_stock(date):
    mill_sfa = mill_storage_flour_accounting.objects.filter(Date_word=date)

    return None