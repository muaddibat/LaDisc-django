from django.shortcuts import render
from django.http import HttpResponse
from store.models import Disc

def home(request):
    discs = Disc.objects.all().filter(is_available=True)

    context = {
        'discs': discs,
    }
    return render(request, 'home.html', context)



