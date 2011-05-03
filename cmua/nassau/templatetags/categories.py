from django import template
from django.db.models import Count

from cmua.nassau.models import Category

register = template.Library()

class CategoryCountNode(template.Node):
    @classmethod
    def handle_token(cls, parser, token):
        tokens = token.contents.split()

        # {% get_top_categories 5 as varname %}
        if len(tokens) != 4:
            raise template.TemplateSyntaxError("get_top_categories tag requires 3 arguments" % tokens[0])

        try:
            n = int(tokens[1])
        except ValueError:
            raise template.TemplateSyntaxError("First argument in get_top_categories must be an integer count of categories to retrieve")

        if tokens[2] != "as":
            raise template.TemplateSyntaxError("Second argument in get_top_categories must be 'as'")

        return cls(n, tokens[3])

    def __init__(self, n, varname):
        self.n = n
        self.varname = varname

    def render(self, context):
        #select the top n blogs ordered by # of blog posts
        context[self.varname] = Category.objects\
                                        .annotate(n_blogs=Count('blogs'))\
                                        .order_by("-n_blogs")[:self.n]
        return ''

@register.tag
def get_top_categories(parser, token):
    """
    gets the top n categories and the number of blogs in them

    Syntax::
        
        {% get_top_categories [n] as [varname] %}

    Example usage::
        
        {% get_top_categories 5 as [categories] %}
        {% for cat in categories %}
            ...
        {% endfor %}
    """
    return CategoryCountNode.handle_token(parser, token)
