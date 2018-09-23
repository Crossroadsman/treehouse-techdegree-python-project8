import random

from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Mineral


def index(request, letter='A', group=None):
    minerals = Mineral.objects.filter(name__startswith=letter)
    template = 'catalog/index.html'
    context = {'minerals': minerals, 'bolded': [letter]}
    return render(request, template, context)

def detail(request, mineral_id):
    mineral = Mineral.objects.get(pk=mineral_id)
    exclude = ['id']
    top_section = ['name', 'image_filename', 'image_caption']
    highlighted = ['category', 'group']


    template = 'catalog/detail.html'
    context = {'mineral': mineral,
               'exclude': exclude,
               'top_section': top_section,
               'highlighted': highlighted,}
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
    context = {'minerals': minerals, 'bolded': [letter]}
    return render(request, template, context)

def group(request, group):
    group_spaces = group.replace('_', ' ')
    minerals = Mineral.objects.filter(group__iexact=group_spaces)
    template = 'catalog/index.html'
    context = {'minerals': minerals, 'bolded': [group]}
    return render(request, template, context)

def search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(
        Q(name__icontains=term)|
        Q(image_caption__icontains=term)|
        Q(category__icontains=term)|
        Q(formula__icontains=term)|
        Q(strunz_classification__icontains=term)|
        Q(crystal_system__icontains=term)|
        Q(unit_cell__icontains=term)|
        Q(color__icontains=term)|
        Q(crystal_symmetry__icontains=term)|
        Q(cleavage__icontains=term)|
        Q(mohs_scale_hardness__icontains=term)|
        Q(luster__icontains=term)|
        Q(streak__icontains=term)|
        Q(diaphaneity__icontains=term)|
        Q(optical_properties__icontains=term)|
        Q(group__icontains=term)|
        Q(refractive_index__icontains=term)|
        Q(crystal_habit__icontains=term)|
        Q(specific_gravity__icontains=term)
    )
    template = 'catalog/index.html'
    context = {'minerals': minerals}
    return render(request, template, context)