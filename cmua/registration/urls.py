from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', "registration.views.index", name="register"),
    url(r'^checkout.html$', "registration.views.checkout", name="checkout"),
)
