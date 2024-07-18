from django.shortcuts import render, get_object_or_404
from .models import Disc
from django.http import HttpResponse
from category.models import Category


# Create your views here.

def store(request, category_slug=None):
    categories = None
    discs = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        discs = Disc.objects.filter(category=categories, is_available=True)
        disc_count = discs.count()
    else:
        discs = Disc.objects.all().filter(is_available=True)
        disc_count = discs.count()

    context = {
        'discs': discs,
        'disc_count': disc_count
    }
    
    return render(request, 'store/store.html', context)

def disc_detail(request, category_slug, disc_slug):
    try:
        single_disc = Disc.objects.get(category__slug=category_slug, slug=disc_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_disc': single_disc,
    }
    return render(request, 'store/disc_detail.html', context)
