from django import template

register = template.Library()

@register.filter
def get_namestatus_task(name):
    if name == 'repairs':
        return 'ремонт'
    elif name == 'maintenance':
        return 'ТО'
    elif name == 'lieby':
        return 'Бездействует'
    else:
        return 'в работе'