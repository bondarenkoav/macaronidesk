from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from account.views import get_cur_factory
from reference_books.models import status_task, typenotification_task
from tasks.forms import form_add_task
from tasks.models import user_task, usertask_filter

content_area = u'Рабочий стол'

@login_required()
@permission_required('tasks.task_list_view', login_url=reverse_lazy('page_error403'))
def getlist_tasks(request):
    if request.user.groups.filter(name__in=['Руководители']):
        tasks_list = user_task.objects.filter(Factory=get_cur_factory(request.user))
    else:
        tasks_list = user_task.objects.filter(Q(author=request.user)|Q(executors__in=request.user.groups.all()))

    task_filter = usertask_filter(request.GET, queryset=tasks_list.distinct('id').order_by('-id'))
    paginator = Paginator(task_filter.qs, 20)
    page = request.GET.get('page')

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return render(request, 'tasks/tasks_list.html', {
        'title': u'Список задач',
        'title_area': u'Задачи',
        'tasks': tasks,
        'page': page,
        'tasks_filter': usertask_filter,
    })

@login_required()
@permission_required('tasks.task_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_task(request, id_item):
    if id_item:
        data_task = user_task.objects.get(id=id_item)
    else:
        data_task = user_task.objects.none()

    form = form_add_task(request.POST or None, user=request.user, instance=id_item and user_task.objects.get(id=id_item))

    if request.POST:
        if form.is_valid():
            new_task = form.save(commit=False)
            if id_item:
                old_data = user_task.objects.get(id=id_item)
                if request.user != old_data.author:
                    new_task.title = old_data.title
                    new_task.description = old_data.description
                    new_task.executors = old_data.executors
                    new_task.Date_limit = old_data.Date_limit
                    new_task.Time_limit = old_data.Time_limit
                    new_task.high_importance = old_data.high_importance
                    if form.cleaned_data.get('status') == status_task.objects.get(slug='complete'):
                        new_task.read = False
                        new_task.status = status_task.objects.get(slug='control')
                else:
                    if form.cleaned_data['confirmation'] == True:
                        new_task.status = status_task.objects.get(slug='confirmation')
                    if form.cleaned_data['status'] == None:
                        new_task.status = old_data.status
                new_task.Update_user = request.user
            else:
                new_task.Factory = get_cur_factory(request.user)
                new_task.author = request.user
                new_task.Create_user = request.user
                new_task.status = status_task.objects.get(slug='open')
            new_task.notification = typenotification_task.objects.get(slug='system')
            new_task.save()
            return redirect('getlist_tasks')
        else:
            return render(request, 'tasks/tasks_one.html', {
                'title': 'Задача №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Задачи',
                'form': form,
                'data_task': data_task})
    else:
        if id_item:
            #request.user.groups.all() == user_task.objects.get(id=id_item).executor:
            if request.user.groups.filter(name=user_task.objects.get(id=id_item).executors).exists():
                user_task.objects.filter(id=id_item).update(read=True)
            data_task = user_task.objects.get(id=id_item)
        else:
            data_task = user_task.objects.none()
        return render(request, 'tasks/tasks_one.html', {
            'title': 'Задача №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Задачи',
            'form': form,
            'data_task': data_task})