from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r'^$', "nassau.views.index", name="blog"),
    url(r'^archive$', "nassau.views.list", name="blog_list"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', "nassau.views.blog_post", name="blog_post"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', "nassau.views.archive", name="blog_archive"),
    url(r'^(?P<year>\d{4})/$', "nassau.views.archive"),
    url(r'^category/(?P<category>[-\w ]+)/$', "nassau.views.category"),
    url(r'^mce_list$', "nassau.views.mce_list", name="images"),
    url(r'^feed', "nassau.views.feed", name="blog_feed"),
)
