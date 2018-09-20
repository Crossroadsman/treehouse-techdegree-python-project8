import random

from django.shortcuts import render, redirect

from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    template = 'catalog/index.html'
    context = {'minerals': minerals}
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
    context = {'minerals': minerals}
    return render(request, template, context)