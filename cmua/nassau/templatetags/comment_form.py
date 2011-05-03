from django import template
from django.template.loader import render_to_string

register = template.Library()

class RenderFormNode(template.Node):
    def render(self, context):
        return render_to_string("blog/comment_form.html", context)

@register.tag
def nassau_render_comment_form(parser, token):
    return RenderFormNode()
