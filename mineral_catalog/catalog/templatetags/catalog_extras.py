from django import template

from catalog.models import Mineral


register = template.Library()

@register.inclusion_tag('catalog/group_nav.html')
def nav_group_list(bolded):
    """Returns the mineral groups to display as a navigation pane"""
    groups = Mineral.objects.order_by().values_list(
        'group', flat=True
    ).distinct()
    groups_ = [x.replace(' ', '_') for x in groups]
    return {'groups': groups_, 'bolded': bolded }

@register.inclusion_tag('catalog/field_nav.html')
def nav_field_list(filter_field, bolded):
    """Returns the group_by to display as a navigation pane"""
    items = Mineral.objects.order_by().values_list(
        filter_field, flat=True
    ).distinct()
    items_ = []
    for item in items:
        if item == '':
            items_.append("None")
        else:
            items_.append(item.replace(' ', '_'))
    return {'field': filter_field, 'items': items_, 'bolded': bolded }


@register.filter('deunderscore')
def deunderscore(text):
    """Replaces underscores with spaces"""
    return text.replace('_', ' ')
