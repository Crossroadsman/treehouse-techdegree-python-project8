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
    return {'groups': groups_, 'bolded': bolded}


@register.filter('deunderscore')
def deunderscore(text):
    """Replaces underscores with spaces"""
    return text.replace('_', ' ')
