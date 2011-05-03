from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, IntegerField, ManyToManyField, Manager, SlugField, ImageField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import comments
from django.contrib.comments import signals
from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib import messages

from imagekit.models import ImageModel

from datetime import datetime

from cmua.colorfield.fields import ColorField

# Create your models here.
class Blog(ImageModel):
    title = CharField(max_length=8192)
    thumbnail = ImageField(upload_to="images/%Y/%m/%d", blank=True)
    content = TextField()
    pub_date = DateTimeField(default=datetime.now)
    add_date = DateTimeField(auto_now_add=True)
    mod_date = DateTimeField(auto_now=True)
    objects = Manager()
    author = ForeignKey(User, related_name="added_posts")
    slug = SlugField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

    def get_absolute_url(self):
        name = "blog_post"
        kwargs = {
            "year": self.pub_date.strftime("%Y"),
            "month": self.pub_date.strftime("%m"),
            "day": self.pub_date.strftime("%d"),
            "slug": self.slug,
        }
        return reverse(name, kwargs=kwargs)

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        # TODO: remove this cmua.?
        spec_module = 'cmua.nassau.specs'
        cache_dir = 'thumbs'
        image_field = 'thumbnail'
	
class Category(Model):
    TAG_COLOR_CHOICES = (
  	  (u'#acc065', u'Green'),
	  (u'#59b6e1', u'Blue'),
	  (u'#ce4545', u'Red'),
	  (u'#838383', u'Grey'),
	  (u'#2b2b2b', u'Dark Grey'),
    )

    name = CharField(max_length=8192)
    #color = ColorField()
    color = CharField(max_length=7, choices=TAG_COLOR_CHOICES)
    blogs = ManyToManyField(Blog, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Image(ImageModel):
    post = models.ForeignKey(Blog, related_name="images")
    image_path = models.ImageField(upload_to="images/%Y/%m/%d")
    url = models.CharField(max_length=150, blank=True)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'cmua.nassau.specs'
        cache_dir = 'thumbs'
        image_field = 'image_path'
    
    def __unicode__(self):
        if self.pk is not None:
            return "{{ Image %d }}" % self.pk
        else:
            return "deleted image"

class BlogModerator(CommentModerator):
    email_notification = True

    def moderate(self, comment, content_object, request):
        return True

moderator.register(Blog, BlogModerator)
