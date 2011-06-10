from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', "cmua.scorereporter.views.index", name="scorereporter"),
)
