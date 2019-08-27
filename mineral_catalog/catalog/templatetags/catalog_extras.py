from django import template

from catalog.models import Mineral


register = template.Library()


@register.inclusion_tag('catalog/field_nav.html')
def nav_field_list(group_lookup, bolded):
    """Returns a list of items to display as a navigation pane"""
    items = group_lookup.list
    items = [x.replace(' ', '_') for x in items]
    return {
        'field': group_lookup.name,
        'items': items,
        'bolded': bolded,
        'range': range(len(items))
    }


@register.filter('deunderscore')
def deunderscore(text):
    """Replaces underscores with spaces"""
    return text.replace('_', ' ')


@register.filter('index')
def index(list, i):
    return list[int(i)]
