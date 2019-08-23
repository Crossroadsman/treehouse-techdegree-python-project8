import random

from django.shortcuts import render, redirect

from .forms import SearchForm
from .models import Mineral
from .group_lookup import groups as FILTER_FIELDS
from .search import full_text_search


def index(request, letter='A', group=None):

    # Note we could have used POST for the form,
    # but GET is better for submissions that don't change state on
    # the server and it allows the user to bookmark a particular search
    if request.GET.get('search_query'):  # a search was submitted

        term = request.GET.get('search_query')
        minerals = full_text_search(term)
        context = {
            'minerals': minerals,
            'filter_fields': FILTER_FIELDS,
            'form': SearchForm()  # clear out the search box
        }

    else:  # regular page load

        minerals = Mineral.objects.filter(name__startswith=letter)
        context = {
            'minerals': minerals,
            'bolded': [letter],
            'filter_fields': FILTER_FIELDS,
            'form': SearchForm(),
        }
    
    template = 'catalog/index.html'
    
    return render(request, template, context)


def detail(request, mineral_id):
    mineral = Mineral.objects.get(pk=mineral_id)
    exclude = ['id']
    top_section = ['name', 'image_filename', 'image_caption']
    highlighted = ['category', 'group']

    template = 'catalog/detail.html'
    context = {
        'mineral': mineral,
        'exclude': exclude,
        'top_section': top_section,
        'highlighted': highlighted,
        'filter_fields': FILTER_FIELDS,
        'form': SearchForm(),
    }
    return render(request, template, context)

def random_mineral(request):
    minerals = Mineral.objects.all()
    count = minerals.count()
    index = random.randrange(count)
    mineral = minerals[index]
    return redirect('catalog:detail', mineral_id=mineral.pk)

def initial_letter(request, letter):
    minerals = Mineral.objects.filter(name__startswith=letter)
    template = 'catalog/index.html'
    context = {
        'minerals': minerals,
        'bolded': [letter],
        'filter_fields': FILTER_FIELDS,
        'form': SearchForm(),
    }
    return render(request, template, context)

def group(request, field, index):
    """Displays a list view which is filtered by a `field` (the valid fields
    are specified by FILTER_FIELDS). Each field has a list of acceptable
    values. `index` specifies the position in that list"""
    field_spaces = field.replace('_', ' ')
    index = int(index)
    group = FILTER_FIELDS[field_spaces]
    minerals = group.get_matching_queryset(index)

    template = 'catalog/index.html'
    context = {
        'minerals': minerals,
        'bolded': [group.list[index]],
        'filter_fields': FILTER_FIELDS,
        'form': SearchForm(),
    }
    return render(request, template, context)
