# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from account.views import get_cur_factory
from dept_okk.forms import *
from dept_okk.models import *


content_area = u'ОКК'
jornal_title_small = u'Журнал'

@login_required
def okk_index(request):
    return render(request, 'dept_okk/okk.html')
# ----------------------------------------------------------------------
#               okk_wheatqualitycontrol
# ----------------------------------------------------------------------
@login_required()
@permission_required('dept_okk.okk_wqc_list_view', login_url=reverse_lazy('page_error403'))
def getlist_okk_wheatqualitycontrol(request):
    query_list = okk_wheat_quality_control.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = okkwheatqualitycontrol_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'dept_okk/jornal/okk_wheatqualitycontrol_list.html', {
        'title': u'Входной контроль качества пшеницы',
        'title_area': content_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('dept_okk.okk_wqc_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_okk_wheatqualitycontrol(request, id_item):
    form = form_okk_wheatqualitycontrol(request.POST or None, instance=id_item and
                                        okk_wheat_quality_control.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('okk:getlist_wheatqualitycontrol')
        else:
            if id_item == None: 'новая'
            return render(request, 'dept_okk/jornal/okk_wheatqualitycontrol_one.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Входной контроль качества пшеницы',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'dept_okk/jornal/okk_wheatqualitycontrol_one.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Входной контроль качества пшеницы',
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               okk_operationalqualitycontrolflour
# ----------------------------------------------------------------------
@login_required()
@permission_required('dept_okk.okk_oqcf_list_view', login_url=reverse_lazy('page_error403'))
def getlist_okk_operationalqualitycontrolflour(request):
    query_list = okk_operational_quality_control_flour.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = okkoperationalqualitycontrolflour_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'dept_okk/jornal/okk_operationalqualitycontrolflour_list.html', {
        'title': u'Оперативный качественный контроль муки на мельнице',
        'title_area': content_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('dept_okk.okk_oqcf_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_okk_operationalqualitycontrolflour(request, id_item):
    form = form_okk_operationalqualitycontrolflour(request.POST or None, instance=id_item and
                                        okk_operational_quality_control_flour.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('okk:getlist_operationalqualitycontrolflour')
        else:
            if id_item == None: 'новая'
            return render(request, 'dept_okk/jornal/okk_operationalqualitycontrolflour_one.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Оперативный качественный контроль муки на мельнице',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'dept_okk/jornal/okk_operationalqualitycontrolflour_one.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Оперативный качественный контроль муки на мельнице',
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               okk_controlgrainmoisture
# ----------------------------------------------------------------------
@login_required()
@permission_required('dept_okk.okk_cgm_list_view', login_url=reverse_lazy('page_error403'))
def getlist_okk_controlgrainmoisture(request):
    query_list = okk_control_grain_moisture.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = okkcontrolgrainmoisture_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'dept_okk/jornal/okk_controlgrainmoisture_list.html', {
        'title': u'Контроль увлажнения зерна на мельнице',
        'title_area': content_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('dept_okk.okk_cgm_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_okk_controlgrainmoisture(request, id_item):
    form = form_okk_controlgrainmoisture(request.POST or None, instance=id_item and
                                         okk_control_grain_moisture.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('okk:getlist_controlgrainmoisture')
        else:
            if id_item == None: 'новая'
            return render(request, 'dept_okk/jornal/okk_controlgrainmoisture_one.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Контроль увлажнения зерна на мельнице',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'dept_okk/jornal/okk_controlgrainmoisture_one.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Контроль увлажнения зерна на мельнице',
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               okk_operationalqualitycontrolsemolina
# ----------------------------------------------------------------------
@login_required()
@permission_required('dept_okk.okk_oqcs_list_view', login_url=reverse_lazy('page_error403'))
def getlist_okk_operationalqualitycontrolsemolina(request):
    query_list = okk_operational_quality_control_semolina.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = okkoperationalqualitycontrolsemolina_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'dept_okk/jornal/okk_operationalqualitycontrolsemolina_list.html', {
        'title': u'Оперативный контроль качества манной муки',
        'title_area': content_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('dept_okk.okk_oqcs_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_okk_operationalqualitycontrolsemolina(request, id_item):
    form = form_okk_operationalqualitycontrolsemolina(request.POST or None, instance=id_item and
                                        okk_operational_quality_control_semolina.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('okk:getlist_operationalqualitycontrolsemolina')
        else:
            if id_item == None: 'новая'
            return render(request, 'dept_okk/jornal/okk_operationalqualitycontrolsemolina_one.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Оперативный контроль качества манной муки',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'dept_okk/jornal/okk_operationalqualitycontrolsemolina_one.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Оперативный контроль качества манной муки',
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               okk_packproductsqualitycontrol
# ----------------------------------------------------------------------
@login_required()
@permission_required('dept_okk.okk_pqc_list_view', login_url=reverse_lazy('page_error403'))
def getlist_okk_packproductsqualitycontrol(request):
    query_list = okk_packproducts_quality_control.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = okkpackproductsqualitycontrol_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'dept_okk/jornal/okk_packproductsqualitycontrol_list.html', {
        'title': u'Контроль качества фасованной продукции',
        'title_area': content_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('dept_okk.okk_pqc_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_okk_packproductsqualitycontrol(request, id_item):
    form = form_okk_packproductsqualitycontrol(request.POST or None, instance=id_item and
                                                okk_packproducts_quality_control.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('okk:getlist_packproductsqualitycontrol')
        else:
            if id_item == None: 'новая'
            return render(request, 'dept_okk/jornal/okk_packproductsqualitycontrol_one.html', {
                'title': 'Партия №%s' % id_item,
                'title_area': content_area,
                'title_small': 'Контроль качества фасованной продукции',
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'dept_okk/jornal/okk_packproductsqualitycontrol_one.html', {
            'title': 'Партия №%s' % id_item,
            'title_area': content_area,
            'title_small': 'Входной контроль качества пшеницы',
            'form': form,
            'id_item': id_item}
        )