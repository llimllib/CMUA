from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^register/', include('cmua.registration.urls')),

    (r'^directions$', direct_to_template, {'template': "directions.html"}),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^$', "nassau.views.index"),
)
