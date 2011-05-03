from django.views.generic.list_detail import object_list
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib import comments
from django.http import HttpResponse
from django.conf import settings
import datetime

from tinymce.views import render_to_image_list

from cmua.nassau.models import Blog, Image, Category
from comment_post import save_comment

def index(request):
    blogs = Blog.objects.all()
    frontpage = True

    return object_list(request,
                       template_name='blog/index.html',
                       template_object_name='blog',
                       queryset=blogs,
                       extra_context=locals(),
                       paginate_by=5)

def list(request):
    blogs = Blog.objects.all()

    return object_list(request,
                       template_name='blog/list.html',
                       template_object_name='blog',
                       queryset=blogs,
                       extra_context=locals(),
                       paginate_by=5)

@csrf_protect
def blog_post(request, **kwargs):
    data = {}

    blogs = Blog.objects.all().filter(
            pub_date__year = int(kwargs["year"]),
            pub_date__month = int(kwargs["month"]),
            pub_date__day = int(kwargs["day"]),
        )
    post = get_object_or_404(blogs, slug=kwargs["slug"])

    if request.method == 'POST':
        data = save_comment(request)
    else:
        data['theform'] = comments.get_form()(post)

    data["post"] = post

    return render_to_response('blog/post.html',
                              data,
                              context_instance=RequestContext(request))

def archive(request, **kwargs):
    blogs = Blog.objects.all().filter(
                pub_date__year = int(kwargs["year"]))

    if "month" in kwargs:
        blogs = blogs.filter(pub_date__month = int(kwargs["month"]))
        month_year = datetime.date(int(kwargs["year"]), int(kwargs["month"]), 1).strftime("%B %Y")
    else:
        month_year = kwargs["year"]

    return object_list(request,
                       template_name='blog/list.html',
                       template_object_name='blog',
                       queryset=blogs,
                       extra_context=locals(),
                       paginate_by=5)

def category(request, **kwargs):
    (category,) = Category.objects.all().filter(name=kwargs["category"])
    blogs = Blog.objects.all().filter(category__name=category.name)

    return object_list(request,
                       template_name='blog/category.html',
                       template_object_name='blog',
                       queryset=blogs,
                       extra_context=locals(),
                       paginate_by=5)

def mce_list(request):
    referer = request.META.get('HTTP_REFERER', '')
    print referer
    objects = Image.objects.all()
    link_list = [(unicode(obj), obj.entry_image.url) for obj in objects]
    return render_to_image_list(link_list)

def feed(request):
    blogs = Blog.objects.all()
    
    current_site = Site.objects.get_current()
    
    feed_title = getattr(settings, "BLOG_FEED_TITLE", "Blog Feed")
    blog_url = "http://%s%s" % (current_site.domain, reverse("blog"))
    url_name = "blog_feed"
    feed_url = "http://%s%s" % (current_site.domain, reverse(url_name))
    
    if blogs:
        feed_updated = blogs[0].pub_date
    else:
        feed_updated = datetime(2009, 8, 1, 0, 0, 0)
    
    atom = render_to_string("blog/atom_feed.xml", {
        "feed_id": feed_url,
        "feed_title": feed_title,
        "blog_url": blog_url,
        "feed_url": feed_url,
        "feed_updated": feed_updated,
        "entries": blogs,
        "current_site": current_site,
    })
    return HttpResponse(atom, mimetype="application/atom+xml")
