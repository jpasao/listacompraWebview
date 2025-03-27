from django import template

register = template.Library()

@register.filter
def for_parent(value, arg):
    return value.all().filter(parentid__exact=arg)