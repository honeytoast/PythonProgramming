#### Grace Hadiyanto
#### e-mail: ifoundparis@gmail.com
#### Assignment 7
#### CS223P

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def escape_newlines(s):
    """
    A filter for escaping new lines so the string's format can be recognized by
    javascript.
    """
    return s.replace('\n','\\n')
