from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import six
from account.forms import change_cur_factory_form
from account.models import Profile
from reference_books.models import Factory
from tasks.models import user_task


def logout(request):
    auth.logout(request)
    return redirect('login')


def get_factory(user):
    return Profile.objects.get(user=user).factory.all()


def get_cur_factory(user):
    profile = Profile.objects.get(user=user)
    # Перестраховка: если вдруг "текущая" и "по умолчанию" не выбраны
    if profile.factory_current:
        cur_factory = profile.factory_current
    elif profile.factory_default:
        cur_factory = profile.factory_default
    else:
        cur_factory = profile.factory.all().first()
    return cur_factory


def group_required(group, login_url=None, raise_exception=False):
    def in_groups(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        if user.is_superuser or bool(user.groups.filter(name__in=groups)):
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(in_groups, login_url=login_url)


def user_profile(request):
    return render(request, 'account/user_profile.html', {
        'profile': Profile.objects.get(user=request.user),      # профиль
        'tasks_incoming': user_task.objects.filter(executor=request.user),      # задачи мне
        'tasks_outgoing': user_task.objects.filter(author=request.user)     # мои задачи
    })


@login_required()
def page_error403(request):
    error_type = '403'
    error_description = 'Вам сюда нельзя'
    return render(request, 'error.html', {'error_type':error_type, 'error_description':error_description})

@login_required()
def page_error423(request):
    error_type = '423'
    error_description = 'Вам не назначена группа прав'
    return render(request, 'error.html', {'error_type':error_type, 'error_description':error_description})

@login_required()
def page_error503(request):
    error_type = '503'
    error_description = 'Сервис недоступен'
    return render(request, 'error.html', {'error_type':error_type, 'error_description':error_description})


# Смена текущей сервисной компании
@login_required()
def change_cur_factory(request):
    form = change_cur_factory_form(request.POST, user=request.user)
    if request.POST:
        if form.is_valid():
            cur_factory = Factory.objects.get(id=int(request.POST['cur_factory']))
            Profile.objects.filter(user=request.user).update(factory_current=cur_factory)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))