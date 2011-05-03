from datetime import datetime

from django import forms

#XXX: what markup to use?
from cmua.nassau.models import Blog

from tinymce.widgets import TinyMCE

from cmua.colorfield.fields import ColorWidget

#This is derived from the AdminPostForm in Biblion. Thanks Biblion guys!
class AdminBlogForm(forms.ModelForm):
    
    title = forms.CharField(
        max_length = 90,
        widget = forms.TextInput(
            attrs = {"style": "width: 50%;"},
        ),
    )
    slug = forms.CharField(
        widget = forms.TextInput(
            attrs = {"style": "width: 50%;"},
        )
    )
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 100, 'rows': 40}, 
            mce_attrs={'theme': 'advanced'}
        )
    )
    
    class Meta:
        model = Blog
    
    def __init__(self, *args, **kwargs):
        super(AdminBlogForm, self).__init__(*args, **kwargs)
        
        post = self.instance
        
    def save(self):
        post = super(AdminBlogForm, self).save(commit=False)
        
        post.published = datetime.now()
        post.updated = datetime.now()
        post.save()
        
        return post

class CategoryBlogForm(forms.ModelForm):
    
    name = forms.CharField(
        max_length = 90,
        widget = forms.TextInput(
            attrs = {"style": "width: 50%;"},
        ),
    )

    color = ColorWidget()
