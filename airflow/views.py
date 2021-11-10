from django.shortcuts import render
from .models import *

# Create your views here.


def fetch_airports(request):
    airport_list = Airport.objects.get(ap_id=0)
    return render(request, 'display.html', {'airport': airport_list})