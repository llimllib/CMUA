from django.contrib import admin
from django.conf import settings
from django.utils.functional import curry

from cmua.nassau.models import Blog, Category, Image
from cmua.nassau.forms import AdminBlogForm, CategoryBlogForm

class ImageInline(admin.TabularInline):
    model = Image
    fields = ["image_path"]

class CategoryInline(admin.TabularInline):
    model = Category.blogs.through
    extra = 0

class BlogAdmin(admin.ModelAdmin):  
    list_display = ["title"]
    form = AdminBlogForm
    fields = [
        "title",
        "slug",
        "author",
        "thumbnail",
        "content",
    ]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        CategoryInline, ImageInline,
    ]
    
    #thanks biblion
    #this doesn't seem to work anymore?
    #def formfield_for_dbfield(self, db_field, **kwargs):
    #    request = kwargs.pop("request")
    #    ff = super(BlogAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    #    import pdb; pdb.set_trace()
    #    if db_field.name == "author":
    #        ff.initial = request.user.id
    #    return ff
    
    def get_form(self, request, obj=None, **kwargs):
        kwargs.update({
            "formfield_callback": curry(self.formfield_for_dbfield, request=request),
        })
        return super(BlogAdmin, self).get_form(request, obj, **kwargs)
    
    def save_form(self, request, form, change):
        # this is done for explicitness that we want form.save to commit
        # form.save doesn't take a commit kwarg for this reason
        return form.save()

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryBlogForm

    def get_form(self, request, obj=None, **kwargs):
        kwargs.update({
            "formfield_callback": curry(self.formfield_for_dbfield, request=request),
        })
        return super(BlogAdmin, self).get_form(request, obj, **kwargs)
    
    def save_form(self, request, form, change):
        # this is done for explicitness that we want form.save to commit
        # form.save doesn't take a commit kwarg for this reason
        return form.save()

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Image)
