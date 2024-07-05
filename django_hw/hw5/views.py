from django.shortcuts import render
from django.utils import timezone
from .models import Icecream

def goods(request):
    icecreams = Icecream.objects.all().order_by('name')
    return render(request, 'blog/base.html', {'kiosks': icecreams})