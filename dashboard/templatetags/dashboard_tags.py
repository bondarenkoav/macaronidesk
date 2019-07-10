from tasks.models import user_task
from dashboard.models import menu
from django import template
from account.forms import change_cur_factory_form

register = template.Library()

__author__ = 'ipman'

@register.inclusion_tag('templatetags/sidebar.html')
def tag_navigation():
    return {'nodes':menu.objects.all()}

@register.inclusion_tag('templatetags/profile_menu.html')
def tag_topbar(user):
    return {'user': user}

@register.inclusion_tag('templatetags/notify.html')
def notify_topbar(user):
    new_tasks = user_task.objects.none()
    if not user.is_superuser:
        new_tasks = user_task.objects.filter(executors__in=user.groups.all(), read=False)
    return {'new_tasks': new_tasks}

@register.inclusion_tag('templatetags/change_factory.html')
def factory_topbar(user):
    return {'user': user, 'form': change_cur_factory_form(user=user)}