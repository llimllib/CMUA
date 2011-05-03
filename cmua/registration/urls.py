from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', "cmua.registration.views.index", name="register"),
    url(r'^checkout.html/(?P<name>.*)$', "cmua.registration.views.checkout", name="checkout"),
)
