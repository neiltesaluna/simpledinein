from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter(name='markdown')
@stringfilter
def markdown_filter(value):
    return markdown.markdown(value, extensions=['md_in_html'])