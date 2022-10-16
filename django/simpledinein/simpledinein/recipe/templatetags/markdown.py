from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter(name='markdown')
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['md_in_html'])