from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.


def fetch_airports(request):
    airport_list = Airport.objects.get(ap_id=0)
    return render(request, 'display_A.html', {'airport': airport_list})


def func(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Done!')
    else:
        form = FlightForm()
        return render(request, 'PrintForm.html', {'form': form})
