from datetime import date
from django.db.models import Q
from production_complex.models import product_work_plan
from reference_books.models import machine_production

__author__ = 'ipman'

from django import template

register = template.Library()

@register.filter
def get_days_restrict(date_start, date_end):
    count_days = date_end - date_start
    return count_days.days+1


@register.inclusion_tag('production_complex/templatetags/pc_workplan_tags.html')
def workplan_tags(date_plan):
    object = []
    tasks_dates = product_work_plan.objects.filter(type_task='tasks', date_start=date_plan)
    #restrict_dates = product_work_plan.objects.filter(type_task='restriction', date_start=date_plan)
    #restrict_dates = product_work_plan.objects.filter(date_start__lte=date_plan, date_end__gte=date_plan, type_task='restriction')
    objects = product_work_plan.objects.filter(Q(date_start=date_plan)|Q(date_start__lte=date_plan, date_end__gte=date_plan))

    #if date_plan == date(2019,4,4):
    for machine in machine_production.objects.all():
        task = objects.filter(equipement=machine)
        if task:
            object.append(task)
        else:
            object.append(None)
        #test = object
    return {
        'tasks': object,
        'equipements': machine_production.objects.all(),
    }