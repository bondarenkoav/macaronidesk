# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import FloatField, Sum, IntegerField, Max
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from account.views import get_cur_factory
from dashboard.models import menu
from mill_complex.forms import *
from mill_complex.models import *
from reference_books.models import BHM, Sil


content_area = u'Мельничное производство'
mill_title_area = u'Мельница'
elevator_title_area = u'Элеватор'
jornal_title_small = u'Журнал'

@login_required
def mill_index(request):
    cat = menu.objects.get(slug='mill')
    link = cat.get_ancestors()
    return render(request, 'mill_complex/mill.html', {
        'list_links': link,
        'content_title': mill_title_area,
        'content_area': content_area,
        'content_title_small': u'Меню',
    })

# ----------------------------------------------------------------------
#               elevator_grain_intake
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_egi_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_elevatorgrainintake(request):
    query_list = elevator_grain_intake.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = elevatorgrainintake_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/elevator/mill_elevatorgrainintake_list.html', {
        'title': u'Журнал учёта прихода зерна',
        'title_area': elevator_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_egi_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_elevatorgrainintake(request, id_item):
    title_small = u'Журнал учёта прихода зерна'
    form = form_mill_elevatorgrainintake(request.POST or None, instance=id_item and
                                         elevator_grain_intake.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_elevatorgrainintake')
    else:
        return render(request, 'mill_complex/jornal/elevator/mill_elevatorgrainintake_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               elevator_grain_waste_accounting
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_egwa_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_elevatorgrainwasteaccounting(request):
    query_list = elevator_grain_waste_accounting.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = elevatorgrainwasteaccounting_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/elevator/mill_elevatorgrainwasteaccounting_list.html', {
        'title': u'Учёт зерноотходов на элеваторе',
        'title_area': elevator_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_egwa_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_elevatorgrainwasteaccounting(request, id_item):
    title_small = u'Журнал учёта муки поступающей на склад'
    form = form_mill_elevatorgrainwasteaccounting(request.POST or None, instance=id_item and
                                               elevator_grain_waste_accounting.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_elevatorgrainwasteaccounting')
    else:
        return render(request, 'mill_complex/jornal/elevator/mill_elevatorgrainwasteaccounting_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               mill_elevatorshipmentwheattomill
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_eswm_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_elevatorshipmentwheattomill(request):
    query_list = elevator_shipment_wheat_to_mill.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = elevatorgrainwasteaccounting_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/elevator/mill_elevatorshipmentwheattomill_list.html', {
        'title': u'Отгрузка пшеницы на мельницу',
        'title_area': elevator_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'data_sil': Sil.objects.all(),
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_eswm_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_elevatorshipmentwheattomill(request, id_item):
    title_small = u'Отгрузка пшеницы на мельницу'
    ParentForm = form_mill_elevatorshipmentwheattomill(request.POST or None, instance=id_item and
                                                       elevator_shipment_wheat_to_mill.objects.get(id=id_item))
    SilFormset = formset_factory(form_mill_elevatorshipmentwheattomill_sil, extra=0)

    if request.POST:
        formset = SilFormset(request.POST)

        if ParentForm.is_valid() and formset.is_valid():
            new_object = ParentForm.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()

            for form in formset:
                sil = form.save(commit=False)
                obj, created = elevator_shipment_wheat_to_mill_child_sil.objects.update_or_create(
                    parent_table=new_object, sil_num=sil.sil_num, defaults=dict(grain=sil.grain, party=sil.party))

            return redirect('mill:getlist_elevatorshipmentwheattomill')
    else:
        data_sil = elevator_shipment_wheat_to_mill_child_sil.objects.none()
        if id_item:
            data_sil = elevator_shipment_wheat_to_mill_child_sil.objects.\
                filter(parent_table=elevator_shipment_wheat_to_mill.objects.get(id=id_item))

            return render(request, 'mill_complex/jornal/elevator/mill_elevatorshipmentwheattomill_one.html', {
                'title': u'Партия №%s' % id_item,
                'title_area': mill_title_area,
                'title_small': title_small,
                'id_item': id_item,
                'form': ParentForm,
                'formset': SilFormset(
                    initial=[
                        {'sil_num': 1, 'grain': data_sil.get(sil_num=1).grain, 'party': data_sil.get(sil_num=1).party},
                        {'sil_num': 2, 'grain': data_sil.get(sil_num=2).grain, 'party': data_sil.get(sil_num=2).party},
                        {'sil_num': 3, 'grain': data_sil.get(sil_num=3).grain, 'party': data_sil.get(sil_num=3).party},
                    ]),
                })
        else:
            return render(request, 'mill_complex/jornal/elevator/mill_elevatorshipmentwheattomill_one.html', {
                'title': u'Партия №%s' % id_item,
                'title_area': mill_title_area,
                'title_small': title_small,
                'id_item': None,
                'form': ParentForm,
                'formset': SilFormset(
                    initial=[
                        {'sil_num': 1, 'grain': '', 'party': 0},
                        {'sil_num': 2, 'grain': '', 'party': 0},
                        {'sil_num': 3, 'grain': '', 'party': 0},
                    ]),
                })
# ----------------------------------------------------------------------
#               mill_bagging
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_bag_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_bagging(request):
    query_list = mill_bagging.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = millbagging_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/mill/mill_bagging_list.html', {
        'title': u'Учёт мешков',
        'title_area': mill_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_bag_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_bagging(request, id_item):
    title_small = u'Учёт мешков'
    form = form_mill_bagging(request.POST or None, instance=id_item and
                                        mill_bagging.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_bagging')
        else:
            if id_item == None: 'новая'
            return render(request, 'mill_complex/jornal/mill/mill_bagging_one.html', {
                'title': u'Партия №%s' % id_item,
                'title_area': mill_title_area,
                'title_small': title_small,
                'form': form,
                'id_item': id_item}
            )
    else:
        return render(request, 'mill_complex/jornal/mill/mill_bagging_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               mill_grainwasteaccounting
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_gwa_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_grainwasteaccounting(request):
    query_list = mill_grain_waste_accounting.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = millgrainwasteaccounting_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/mill/mill_grainwasteaccounting_list.html', {
        'title': u'Учёт зерна/отходов',
        'title_area': mill_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_gwa_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_grainwasteaccounting(request, id_item):
    title_small = u'Учёт зерноотходов'
    form = form_mill_grainwasteaccounting(request.POST or None, instance=id_item and
                                         mill_grain_waste_accounting.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_grainwasteaccounting')
    else:
        return render(request, 'mill_complex/jornal/mill/mill_grainwasteaccounting_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               mill_controlmagneticinstallations
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_cmi_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_controlmagneticinstallations(request):
    query_list = mill_control_magnetic_installations.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = millcontrolmagneticinstallations_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/mill/mill_controlmagneticinstallations_list.html', {
        'title': u'Контроль магнитных установок',
        'title_area': mill_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_cmi_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_controlmagneticinstallations(request, id_item):
    title_small = u'Контроль магнитных установок'
    form = form_mill_controlmagneticinstallations(request.POST or None, instance=id_item and
                                        mill_control_magnetic_installations.objects.get(id=id_item))
    if request.method == 'POST':
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_controlmagneticinstallations')
    else:
        return render(request, 'mill_complex/jornal/mill/mill_controlmagneticinstallations_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               mill_laboratorywork
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_lw_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_laboratorywork(request):
    query_list = mill_laboratory_work.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = milllaboratorywork_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/mill/mill_laboratorywork_list.html', {
        'title': u'Лабораторные работы',
        'title_area': mill_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_lw_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_laboratorywork(request, id_item):
    title_small = u'Журнал лабораторных работ'
    form = form_mill_laboratorywork(request.POST or None, instance=id_item and
                                                mill_laboratory_work.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_laboratorywork')
    else:
        return render(request, 'mill_complex/jornal/mill/mill_laboratorywork_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               mill_technological
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_tech_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_technological(request):
    query_list = mill_technological.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = milltechnological_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/mill/mill_technological_list.html', {
        'title': u'Технологический журнал',
        'title_area': mill_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'data_bhm': BHM.objects.all(),
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_tech_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_technological(request, id_item):
    title_small = u'Технологический журнал'

    ParentForm = form_mill_technological(request.POST or None, instance=id_item and mill_technological.objects.get(id=id_item))
    BHMFormset = formset_factory(form_mill_technological_bhm, extra=0)

    if request.POST:
        formset = BHMFormset(request.POST)

        if ParentForm.is_valid() and formset.is_valid():
            new_object = ParentForm.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()

            try:
                knockedout_topgrade = (new_object.KnockedOut_TopGrade_stop - new_object.KnockedOut_TopGrade_start) + 1
                mill_technological.objects.filter(id=id_item).update(KnockedOut_TopGrade=knockedout_topgrade)
            except:
                pass

            for form in formset:
                bhm = form.save(commit=False)
                obj, created = mill_technological_child_bhm.objects.update_or_create(
                    parent_table=new_object, bhm_num=bhm.bhm_num, defaults=dict(grain=bhm.grain))

            return redirect('mill:getlist_technological')
    else:
        data_bhm = mill_technological_child_bhm.objects.none()
        if id_item:
            data_bhm = mill_technological_child_bhm.objects.\
                filter(parent_table=mill_technological.objects.get(id=id_item))

            return render(request, 'mill_complex/jornal/mill/mill_technological_one.html', {
                'title': u'Партия №%s' % id_item,
                'title_area': mill_title_area,
                'title_small': title_small,
                'id_item': id_item,
                'form': ParentForm,
                'formset': BHMFormset(
                    initial=[
                        {'bhm_num': 1, 'grain': data_bhm.get(bhm_num=1).grain},
                        {'bhm_num': 2, 'grain': data_bhm.get(bhm_num=2).grain},
                        {'bhm_num': 3, 'grain': data_bhm.get(bhm_num=3).grain},
                        {'bhm_num': 4, 'grain': data_bhm.get(bhm_num=4).grain},
                    ]),
                })
        else:
            return render(request, 'mill_complex/jornal/mill/mill_technological_one.html', {
                'title': u'Партия №%s' % id_item,
                'title_area': mill_title_area,
                'title_small': title_small,
                'id_item': None,
                'form': ParentForm,
                'formset': BHMFormset(
                    initial=[
                        {'bhm_num': 1, 'grain': ''},
                        {'bhm_num': 2, 'grain': ''},
                        {'bhm_num': 3, 'grain': ''},
                        {'bhm_num': 4, 'grain': ''},
                    ]),
                })

# ----------------------------------------------------------------------
#               mill_storage_flour_accounting
# ----------------------------------------------------------------------
@login_required()
@permission_required('mill_complex.m_sfa_list_view', login_url=reverse_lazy('page_error403'))
def getlist_mill_storageflouraccounting(request):
    query_list = mill_storage_flour_accounting.objects.filter(Factory=get_cur_factory(request.user))

    query_filter = millstorageflouraccounting_filter(request.GET, queryset=query_list.distinct('id').order_by('-id'))
    paginator = Paginator(query_filter.qs, 15)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request, 'mill_complex/jornal/mill/mill_storageflouraccounting_list.html', {
        'title': u'Журнал учёта муки поступающей на склад',
        'title_area': mill_title_area,
        'title_small': jornal_title_small,
        'list': list,
        'list_filter': query_filter,
        'page': page
    })

@login_required()
@permission_required('mill_complex.m_sfa_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_mill_storageflouraccounting(request, id_item):
    title_small = u'Журнал учёта муки поступающей на склад'
    form = form_mill_storageflouraccounting(request.POST or None, instance=id_item and
                                               mill_storage_flour_accounting.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            new_object = form.save(commit=False)
            if id_item == None:
                new_object.Create_user = request.user
                new_object.Factory = get_cur_factory(request.user)
            else:
                new_object.Update_user = request.user
            new_object.save()
            return redirect('mill:getlist_storageflouraccounting')
    else:
        return render(request, 'mill_complex/jornal/mill/mill_storageflouraccounting_one.html', {
            'title': u'Партия №%s' % id_item,
            'title_area': mill_title_area,
            'title_small': title_small,
            'form': form,
            'id_item': id_item}
        )
# ----------------------------------------------------------------------
#               О Т Ч Е Т Ы
# ----------------------------------------------------------------------
@login_required()
def report_mill_count_graininsilos(request):
    return render(request, 'mill_complex/reports/count_graininsilos.html', {
        'silos': elevator_shipment_wheat_to_mill.objects.values('Sil_1','Sil_2','Sil_3').order_by('-Date_word','-Time_word')[:1]
    })

def report_mill_count_millbagging(request):
    bagging = mill_bagging.objects.filter(Factory=get_cur_factory(request.user),
                                          Date_word__month=datetime.today().month,
                                          Date_word__year=datetime.today().year)
    return render(request, 'mill_complex/reports/count_millbagging.html', {
        'bagging': bagging.order_by('Date_word','Time_word'),
        'total_ReceivedBags_flour': bagging.aggregate(summ=Sum('ReceivedBags_flour')),
        'total_ReceivedBags_zo': bagging.aggregate(summ=Sum('ReceivedBags_zo')),
        'total_ReceivedBags_zelen': bagging.aggregate(summ=Sum('ReceivedBags_zelen')),
    })

def report_mill_daily(request):
    form = form_report_mill_daily(request.POST or None)

    if request.POST:
        if form.is_valid():
            filter_date = form.cleaned_data['filter_date']
            # Отгружено на мельницу
            delivery_wheat = elevator_shipment_wheat_to_mill_child_sil.objects.\
                filter(parent_table__in=elevator_shipment_wheat_to_mill.objects.filter(Date_word=filter_date)).\
                aggregate(ct=Sum('grain', output_field=FloatField()))
            delivery_wheat = int(0 if delivery_wheat['ct'] is None else delivery_wheat['ct'])

            data_mt = mill_technological.objects.filter(Date_word=filter_date).order_by('DateTime_add')

            data_gwa = elevator_grain_waste_accounting.objects.filter(Date_word=filter_date)

            # Произведено
            prod_semolina = data_mt.aggregate(ct=Sum('Prod_Semolina', output_field=IntegerField()))
            prod_semolina = int(0 if prod_semolina['ct'] is None else prod_semolina['ct'])

            data_mt_enum = data_mt.last()
            data_mt_previos_day = mill_technological.objects.filter(Date_word__lt=filter_date).order_by('DateTime_add').last()

            prod_topgrade_total = data_mt_enum.Prod_TopGrade_enum - data_mt_previos_day.Prod_TopGrade_enum
            prod_secondgrade_total = data_mt_enum.Prod_SecondGrade_enum - data_mt_previos_day.Prod_SecondGrade_enum
            prod_bran_total = data_mt_enum.Prod_Bran_enum - data_mt_previos_day.Prod_Bran_enum

            prod_grainwaste = data_mt.aggregate(ct=Sum('Prod_GrainWaste', output_field=IntegerField()))
            prod_grainwaste = int(0 if prod_grainwaste['ct'] is None else prod_grainwaste['ct'])

            prod_bransecondgrade = data_mt.aggregate(ct=Sum('Prod_Bran2Varieties', output_field=IntegerField()))
            prod_bransecondgrade = int(0 if prod_bransecondgrade['ct'] is None else prod_bransecondgrade['ct'])

            prod_grainwaste_firstgrade = data_gwa.aggregate(ct=Sum('GrainWasteTopGrade', output_field=IntegerField()))
            prod_grainwaste_firstgrade = int(0 if prod_grainwaste_firstgrade['ct'] is None else prod_grainwaste_firstgrade['ct'])

            prod_grainwaste_secondgrade = data_gwa.aggregate(ct=Sum('GrainWasteSecondGrade', output_field=IntegerField()))
            prod_grainwaste_secondgrade = int(0 if prod_grainwaste_secondgrade['ct'] is None else prod_grainwaste_secondgrade['ct'])

            # Выбито в мешки
            knock_topdgrade = data_mt.aggregate(ct=Sum('KnockedOut_TopGrade', output_field=IntegerField()))
            knock_topdgrade = int(0 if knock_topdgrade['ct'] is None else knock_topdgrade['ct'])

            knock_secondgrade = data_mt.aggregate(ct=Sum('KnockedOut_SecondGrade', output_field=IntegerField()))
            knock_secondgrade = int(0 if knock_secondgrade['ct'] is None else knock_secondgrade['ct'])

            knock_semolina = data_mt.aggregate(ct=Sum('KnockedOut_Semolina', output_field=IntegerField()))
            knock_semolina = int(0 if knock_semolina['ct'] is None else knock_semolina['ct'])

            # Перемещено
            data_transport = mill_storage_flour_accounting.objects.filter(Date_word=filter_date)

            transport_topgrade = data_transport.aggregate(ct=Sum('TransportTopGrade', output_field=IntegerField()))
            transport_topgrade = int(0 if transport_topgrade['ct'] is None else transport_topgrade['ct'])

            transport_secondgrade = data_transport.aggregate(ct=Sum('TransportSecondGrade', output_field=IntegerField()))
            transport_secondgrade = int(0 if transport_secondgrade['ct'] is None else transport_secondgrade['ct'])

            trans_storage_topgrade = data_transport.aggregate(ct=Sum('TopGrade', output_field=IntegerField()))
            trans_storage_topgrade = int(0 if trans_storage_topgrade['ct'] is None else trans_storage_topgrade['ct'])

            trans_storage_secondgrade = data_transport.aggregate(ct=Sum('SecondGrade', output_field=IntegerField()))
            trans_storage_secondgrade = int(0 if trans_storage_secondgrade['ct'] is None else trans_storage_secondgrade['ct'])

            trans_storage_semolina = data_transport.aggregate(ct=Sum('Semolina', output_field=IntegerField()))
            trans_storage_semolina = int(0 if trans_storage_semolina['ct'] is None else trans_storage_semolina['ct'])

            trans_workshop_topgrade = data_mt_enum.Trans_Workshop - data_mt_previos_day.Trans_Workshop
                #data_mt.aggregate(ct=Sum('Trans_Workshop', output_field=IntegerField()))
            #trans_workshop_topgrade = int(0 if trans_workshop_topgrade['ct'] is None else trans_workshop_topgrade['ct'])

            consumption_grain = prod_semolina + prod_topgrade_total + prod_secondgrade_total + prod_bran_total + \
                                prod_grainwaste + prod_bransecondgrade + prod_grainwaste_firstgrade + prod_grainwaste_secondgrade

            consumption_bag = round((knock_topdgrade + knock_secondgrade + knock_semolina)/50)

            consumption_waste = prod_grainwaste + prod_bransecondgrade

            residue_grain = delivery_wheat - consumption_grain

            residue_topgrade = prod_topgrade_total - (trans_workshop_topgrade + trans_storage_topgrade)

            residue_secondgrade = prod_secondgrade_total - trans_storage_secondgrade

            residue_semolina = prod_semolina - trans_storage_semolina

            transport = transport_topgrade + transport_secondgrade

            return render(request, 'mill_complex/reports/mill_daily.html', {
                'form': form,
                'list': mill_technological.objects.filter(Date_word=filter_date),
                'delivery_wheat': delivery_wheat,
                'filter_date': filter_date,
                # Произведено
                'prod_semolina': prod_semolina,
                'prod_topgrade': prod_topgrade_total,
                'prod_secondgrade': prod_secondgrade_total,
                'prod_bran_enum': prod_bran_total,
                'prod_grainwaste': prod_grainwaste,
                'prod_grainwaste_firstgrade': prod_grainwaste_firstgrade,
                'prod_grainwaste_secondgrade': prod_grainwaste_secondgrade,
                'prod_bransecondgrade': prod_bransecondgrade,
                # Выбито
                'knock_topdgrade': knock_topdgrade,
                'knock_secondgrade': knock_secondgrade,
                'knock_semolina': knock_semolina,
                # Израсходовано
                'consumption_grain': consumption_grain,
                'consumption_bag': consumption_bag,
                'consumption_waste': consumption_waste,
                # Остаток
                'residue_grain': residue_grain,
                'residue_topgrade': residue_topgrade,
                'residue_secondgrade': residue_secondgrade,
                'residue_semolina': residue_semolina,
                # Перемещение
                'trans_storage_topgrade': trans_storage_topgrade,
                'trans_storage_secondgrade': trans_storage_secondgrade,
                'trans_storage_semolina': trans_storage_semolina,
                'trans_workshop_topgrade': trans_workshop_topgrade,
                'transport': transport,
            })
    else:
        return render(request, 'mill_complex/reports/mill_daily.html', {
            'form': form,
        })


def report_mill_grainwasteaccounting(request):
    form = form_report_mill_grainwasteaccounting(request.POST or None)

    if request.POST:
        if form.is_valid():
            filter_start_date = form.cleaned_data['filter_start_date']
            filter_end_date = form.cleaned_data['filter_end_date']
            date_generated = [filter_start_date + timedelta(days=x) for x in range(0, ((filter_end_date+timedelta(days=1))-filter_start_date).days)]

            mill_egwa = elevator_grain_waste_accounting.objects.\
                filter(Date_word__gte=filter_start_date, Date_word__lte=filter_end_date)
            mill_egwa_grainwaste = mill_egwa.aggregate(ct=Sum('GrainWaste', output_field=IntegerField()))
            total_mill_egwa_grainwaste = int(0 if mill_egwa_grainwaste['ct'] is None else mill_egwa_grainwaste['ct'])
            mill_egwa_grainwaste_firstgrade = mill_egwa.aggregate(ct=Sum('GrainWasteTopGrade', output_field=IntegerField()))
            total_mill_egwa_grainwaste_firstgrade = int(0 if mill_egwa_grainwaste_firstgrade['ct'] is None else mill_egwa_grainwaste_firstgrade['ct'])
            mill_egwa_grainwaste_secondgrade = mill_egwa.aggregate(ct=Sum('GrainWasteSecondGrade', output_field=IntegerField()))
            total_mill_egwa_grainwaste_secondgrade = int(0 if mill_egwa_grainwaste_secondgrade['ct'] is None else mill_egwa_grainwaste_secondgrade['ct'])

            mill_gwa = mill_grain_waste_accounting.objects.\
                           filter(Date_word__gte=filter_start_date, Date_word__lte=filter_end_date)
            mill_gwa_bran = mill_gwa.aggregate(ct=Sum('Bran', output_field=IntegerField()))
            total_mill_gwa_bran = int(0 if mill_gwa_bran['ct'] is None else mill_gwa_bran['ct'])
            mill_gwa_secondbran = mill_gwa.aggregate(ct=Sum('BranSecondGrade', output_field=IntegerField()))
            total_mill_gwa_secondbran = int(0 if mill_gwa_secondbran['ct'] is None else mill_gwa_secondbran['ct'])

            mill_sfa = mill_storage_flour_accounting.objects.filter(Date_word__gte=filter_start_date,
                                                                    Date_word__lte=filter_end_date)

            return render(request, 'mill_complex/reports/mill_grainwasteaccounting.html', {
                'form': form,
                'list_date': date_generated,
                'total_mill_egwa_grainwaste': total_mill_egwa_grainwaste,
                'total_mill_egwa_grainwaste_firstgrade': total_mill_egwa_grainwaste_firstgrade,
                'total_mill_egwa_grainwaste_secondgrade': total_mill_egwa_grainwaste_secondgrade,
                'total_mill_gwa_bran': total_mill_gwa_bran,
                'total_mill_gwa_secondbran': total_mill_gwa_secondbran,
            })
    else:
        return render(request, 'mill_complex/reports/mill_grainwasteaccounting.html', {
            'form': form,
        })


def report_mill_grainconsumption(request):
    form = form_report_mill_grainconsumption(request.POST or None)

    if request.POST:
        if form.is_valid():
            filter_start_date = form.cleaned_data['filter_start_date']
            filter_end_date = form.cleaned_data['filter_end_date']
            date_generated = [filter_start_date + timedelta(days=x) for x in range(0, ((filter_end_date+timedelta(days=1))-filter_start_date).days)]

            intake = elevator_grain_intake.objects.filter(Date_word__gte=filter_start_date, Date_word__lte=filter_end_date).\
                aggregate(ct=Sum('WeightCredit', output_field=IntegerField()))
            total_intake = int(0 if intake['ct'] is None else intake['ct'])

            return render(request, 'mill_complex/reports/mill_grainconsumption.html', {
                'form': form,
                'list_date': date_generated,
                'total_intake': total_intake,
                #'total_consumption': total_consumption,
            })
    else:
        return render(request, 'mill_complex/reports/mill_grainconsumption.html', {
            'form': form,
        })