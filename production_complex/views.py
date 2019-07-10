# -*- coding: utf-8 -*-
import calendar

from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from account.views import get_cur_factory
from production_complex.forms import form_pc_lineoperator, form_pc_packingequipmentadjuster, \
    form_pc_equipmentbreakdownrepair, form_add_workplan, form_add_restriction, form_workplan
from production_complex.models import product_line_operator, product_packing_equipment_adjuster, \
    product_equipment_breakdown_repair, product_work_plan, productlineoperator_filter, \
    productpackingequipmentadjuster_filter, productequipmentbreakdownrepair_filter
from reference_books.models import machine_production

content_area = u'Производственный комплекс'
production_title_area = u'Производственный комплекс'
jornal_title_small = u'Журнал'

@login_required
def pc_index(request):
    return render(request, 'production_complex/pc.html')

@login_required()
def add_work_plan(request):
    form = form_add_workplan(request.POST or None)
    if request.POST:
        if form.is_valid():
            new_plan = form.save(commit=False)
            new_plan.Create_user = request.user
            new_plan.end = form.cleaned_data['date_start']+timedelta(days=1)
            new_plan.type_task = 'tasks'
            new_plan.save()
            form.save_m2m()
            return redirect('pc:work_plan')
        else:
            return render(request, 'production_complex/add_plan.html', {'form': form})
    else:
        return render(request, 'production_complex/add_plan.html', {'form': form})

@login_required()
def add_work_restriction(request):
    form = form_add_restriction(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_restriction = form.save(commit=False)
            new_restriction.Create_user = request.user
            if form.cleaned_data['date_end'] == None:
                new_restriction.end = form.cleaned_data['date_start']+timedelta(days=1)
            new_restriction.type_task = 'restriction'
            new_restriction.save()
            form.save_m2m()
            return redirect('pc:work_plan')
        else:
            return render(request, 'production_complex/add_restriction.html', {'form': form})
    else:
        return render(request, 'production_complex/add_restriction.html', {'form': form})

@login_required()
def work_plan(request):
    form = form_workplan(request.POST or None)

    if request.POST:
        if form.is_valid():
            get_year = form.cleaned_data.get('year_plan')
            get_month = form.cleaned_data.get('month_plan')
            date_start = date(get_year, get_month, 1)
            date_end = date(get_year, get_month, calendar.monthrange(datetime.now().year,datetime.now().month)[1])
    else:
        date_start = date(datetime.now().year, datetime.now().month, 1)
        date_end = date(datetime.now().year, datetime.now().month, calendar.monthrange(datetime.now().year,datetime.now().month)[1])

    return render(request, 'production_complex/work_plan_new.html', {
        'form': form,
        'equipement': machine_production.objects.all(),
        'list_date': [date_start + timedelta(days=x) for x in range(0, ((date_end+timedelta(days=1))-date_start).days)],
    })
# ----------------------------------------------------------------------
#               pc_lineoperator
# ----------------------------------------------------------------------
@login_required()
@permission_required('production_complex.p_lo_list_view', login_url=reverse_lazy('page_error403'))
def getlist_pc_productlineoperator(request):
    query_list = product_line_operator.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = productlineoperator_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'production_complex/pc_lineoperator_list.html', {
        'title': u'Журнал оператора линий Бюлер',
        'title_area': production_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })



@login_required()
@permission_required('production_complex.p_lo_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_pc_productlineoperator(request, id_item):
    form = form_pc_lineoperator(request.POST or None, instance=id_item and product_line_operator.objects.get(id=id_item))

    if request.POST:
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('pc:getlist_lineoperator')
        else:
            if id_item == None: 'новая'
            return render(request, 'production_complex/pc_lineoperator_item.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Журнал оператора линий Бюлер',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'production_complex/pc_lineoperator_item.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Журнал оператора линий Бюлер',
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               pc_packingequipmentadjuster
# ----------------------------------------------------------------------
@login_required()
@permission_required('production_complex.p_pea_list_view', login_url=reverse_lazy('page_error403'))
def getlist_pc_packingequipmentadjuster(request):
    query_list = product_packing_equipment_adjuster.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = productpackingequipmentadjuster_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'production_complex/pc_packingequipmentadjuster_list.html', {
        'title': u'Журнал наладчика фасовочного оборудования',
        'title_area': production_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('production_complex.p_pea_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_pc_packingequipmentadjuster(request, id_item):
    form = form_pc_packingequipmentadjuster(request.POST or None, instance=id_item and
                                product_packing_equipment_adjuster.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('pc:getlist_packingequipmentadjuster')
        else:
            if id_item == None: 'новая'
            return render(request, 'production_complex/pc_packingequipmentadjuster_item.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Журнал наладчика фасовочного оборудования',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'production_complex/pc_packingequipmentadjuster_item.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Журнал наладчика фасовочного оборудования',
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               pc_equipmentbreakdownrepair
# ----------------------------------------------------------------------
@login_required()
@permission_required('production_complex.p_ebr_list_view', login_url=reverse_lazy('page_error403'))
def getlist_pc_equipmentbreakdownrepair(request):
    query_list = product_equipment_breakdown_repair.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = productequipmentbreakdownrepair_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'production_complex/pc_equipmentbreakdownrepair_list.html', {
        'title': u'Учет поломок и ремонта оборудования',
        'title_area': production_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('production_complex.p_ebr_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_pc_equipmentbreakdownrepair(request, id_item):
    form = form_pc_equipmentbreakdownrepair(request.POST or None, instance=id_item and
                                product_equipment_breakdown_repair.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('pc:getlist_equipmentbreakdownrepair')
        else:
            if id_item == None: 'новая'
            return render(request, 'production_complex/pc_equipmentbreakdownrepair_item.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Учет поломок и ремонта оборудования',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'production_complex/pc_equipmentbreakdownrepair_item.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Учет поломок и ремонта оборудования',
            'form': form,
            'id_item': id_item}
        )