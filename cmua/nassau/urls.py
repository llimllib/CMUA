from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r'^$', "cmua.nassau.views.index", name="blog"),
    url(r'^archive$', "cmua.nassau.views.list", name="blog_list"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', "cmua.nassau.views.blog_post", name="blog_post"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', "cmua.nassau.views.archive", name="blog_archive"),
    url(r'^(?P<year>\d{4})/$', "cmua.nassau.views.archive"),
    url(r'^category/(?P<category>[-\w ]+)/$', "cmua.nassau.views.category"),
    url(r'^mce_list$', "cmua.nassau.views.mce_list", name="images"),
    url(r'^feed', "cmua.nassau.views.feed", name="blog_feed"),
)
