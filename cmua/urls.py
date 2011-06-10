from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^register/', include('cmua.registration.urls')),
    (r'^report_score/', include('cmua.scorereporter.urls')),

    (r'^directions$', direct_to_template, {'template': "directions.html"}),

    (r'^admin/(?P<app_label>[\d\w]+)/(?P<model_name>[\d\w]+)/csv/', 'cmua.csv_view.actions.admin_list_export'),
    (r'^admin/', include(admin.site.urls)),

    (r'^blog/', include("cmua.nassau.urls")),
    (r'^$', "cmua.nassau.views.index"),
)
