from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from dashboard.models import menu
from reference_books.forms import form_client, form_post, form_product
from reference_books.models import posts, partner, products

content_area = u'Справочники'
title_area = u'Справочники'
title_small = u''

@login_required
def rb_index(request):
    cat = menu.objects.get(slug='mill')
    link = cat.get_ancestors()
    return render(request, 'reference_books/rbooks.html', {
        'list_links': link,
        'content_title': title_area,
        'content_area': content_area,
        'content_title_small': u'Меню',
    })

# ----------------------------------------------------------------------
#               clients
# ----------------------------------------------------------------------
@login_required()
#@permission_required('rbooks_complex.m_egi_list_view', login_url=reverse_lazy('page_error403'))
def getlist_rb_clients(request):
    return render(request, 'reference_books/clients_list.html', {
        'title': u'Контрагенты',
        'title_area': title_area,
        'title_small': title_small,
        'list': partner.objects.all()
    })

@login_required()
#@permission_required('rbooks_complex.m_egi_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_rb_client(request, id_item):
    title_small = u'Контрагент'
    form = form_client(request.POST or None, instance=id_item and partner.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('rbooks:getlist_clients')
    else:
        return render(request, 'reference_books/template_item.html', {
            'title': u'%s' % id_item,
            'title_area': title_area,
            'title_small': title_small,
            'url_getlist': 'rbooks:getlist_clients',
            'url_addget': 'rbooks:addget_client',
            'form': form,
            'id_item': id_item}
        )

# ----------------------------------------------------------------------
#               posts
# ----------------------------------------------------------------------
@login_required()
#@permission_required('rbooks_complex.m_egi_list_view', login_url=reverse_lazy('page_error403'))
def getlist_rb_posts(request):
    return render(request, 'reference_books/posts_list.html', {
        'title': u'Должности',
        'title_area': title_area,
        'title_small': title_small,
        'list': posts.objects.all()
    })

@login_required()
#@permission_required('rbooks_complex.m_egi_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_rb_post(request, id_item):
    title_small = u'Должность'
    form = form_post(request.POST or None, instance=id_item and posts.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('rbooks:getlist_posts')
    else:
        return render(request, 'reference_books/template_item.html', {
            'title': u'%s' % id_item,
            'title_area': title_area,
            'title_small': title_small,
            'url_getlist': 'rbooks:getlist_posts',
            'url_addget': 'rbooks:addget_post',
            'form': form,
            'id_item': id_item}
        )

# ----------------------------------------------------------------------
#               products
# ----------------------------------------------------------------------
@login_required()
#@permission_required('rbooks_complex.m_egi_list_view', login_url=reverse_lazy('page_error403'))
def getlist_rb_products(request):
    return render(request, 'reference_books/products_list.html', {
        'title': u'Продукция',
        'title_area': title_area,
        'title_small': title_small,
        'list': products.objects.all()
    })

@login_required()
#@permission_required('rbooks_complex.m_egi_item_view', login_url=reverse_lazy('page_error403'))
@csrf_protect
def addget_rb_product(request, id_item):
    title_small = u'Продукт'
    form = form_product(request.POST or None, instance=id_item and products.objects.get(id=id_item))
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('rbooks:getlist_products')
    else:
        return render(request, 'reference_books/template_item.html', {
            'title': u'%s' % id_item,
            'title_area': title_area,
            'title_small': title_small,
            'url_getlist': 'rbooks:getlist_products',
            'url_addget': 'rbooks:addget_product',
            'form': form,
            'id_item': id_item}
        )