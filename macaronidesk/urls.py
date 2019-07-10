from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from account.views import user_profile, page_error403, page_error423, page_error503, change_cur_factory
from dashboard.views import index, mylogin, mylogout
from mill_complex.views import report_mill_count_graininsilos, report_mill_count_millbagging, \
    report_mill_grainwasteaccounting, report_mill_daily, report_mill_grainconsumption
from tasks.views import getlist_tasks, addget_task


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', mylogin, name='login'),
    url(r'^accounts/logout/$', mylogout, name='logout'),
    url(r'^accounts/profile/$', RedirectView.as_view(url=('/'))),
    url(r'^profile/$', user_profile, name='profile'),

    url(r'^page_error403', page_error403, name="page_error403"),
    url(r'^page_error423', page_error423, name="page_error423"),
    url(r'^page_error503', page_error503, name="page_error503"),

    url(r'^change_factory/', change_cur_factory, name='change_cur_factory'),

    url(r'^tasks/item/(?:(?P<id_item>\d+)/)?$', addget_task, name='addget_tasks'),
    url(r'^tasks/$', getlist_tasks, name='getlist_tasks'),

    url(r'^okk/', include('dept_okk.urls', namespace='okk')),
    url(r'^production/', include('production_complex.urls', namespace='pc')),
    url(r'^mill/', include('mill_complex.urls', namespace='mill')),

    url(r'^rbooks/', include('reference_books.urls', namespace='rbooks')),

    # Отчеты
    url(r'^reports/grain_in_silos/', report_mill_count_graininsilos, name='report_mill_count_graininsilos'),
    url(r'^reports/mill_bagging/', report_mill_count_millbagging, name='report_mill_count_millbagging'),
    url(r'^reports/mill_daily/', report_mill_daily, name='report_mill_daily'),
    url(r'^reports/mill_gwa/', report_mill_grainwasteaccounting, name='report_mill_grainwasteaccounting'),
    url(r'^reports/mill_gc/', report_mill_grainconsumption, name='report_mill_grainconsumption'),

    url(r'^', index , name='dashboard'),
]