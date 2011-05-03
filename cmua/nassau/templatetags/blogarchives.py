from django import template
from django.db import connection
import datetime

register = template.Library()

class BlogCountNode(template.Node):
    @classmethod
    def handle_token(cls, parser, token):
        tokens = token.contents.split()

        # {% get_archive_count as varname %}
        if len(tokens) != 3:
            raise template.TemplateSyntaxError("get_archive_count tag requires 2 arguments" % tokens[0])

        if tokens[1] != "as":
            raise template.TemplateSyntaxError("Second argument in get_archive_count must be 'as'")

        return cls(tokens[2])

    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        def mkdate(str):
            (month, year) = str.split('/')
            d = datetime.date(int(year), int(month), 1)
            return d
			
    	c = connection.cursor()
        sql = """
			SELECT TO_CHAR(pub_date, 'MM/YYYY') AS month_year, COUNT(*) 
			FROM nassau_blog 
			GROUP BY TO_CHAR(pub_date, 'MM/YYYY')
			ORDER BY TO_CHAR(pub_date, 'MM/YYYY')"""
        c.execute(sql)
        context[self.varname] = map(lambda r: [mkdate(r[0]), r[1]], c)
        return ''

@register.tag
def get_archive_count(parser, token):
    """
    gets a count of blog posts made each month

    Syntax::
        
        {% get_archive_count as [varname] %}

    Example usage::
        
        {% get_archive_count as [archive_list] %}
        {% for month, post_count in archive_list %}
            ...
        {% endfor %}
    """
    return BlogCountNode.handle_token(parser, token)
