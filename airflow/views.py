from django.shortcuts import render
from .forms import *
from django.http import HttpResponse

# Create your views here.


def is_valid(t):
    return t != '' and t is not None


def flight_show(request):
    qset = Flight.objects.all()
    al_list = list(set([str(t.airline) for t in qset]))
    if request.method == 'POST':
        return render(request, "flight/flight_form.html", {'queryset': qset, 'a_ch': al_list})
    else:
        dep_ap = request.GET.get('dep_ap')
        arr_ap = request.GET.get('arr_ap')
        datetime_min = request.GET.get('datetime_min')
        datetime_max = request.GET.get('datetime_max')
        airline = request.GET.get('airline')
        if is_valid(datetime_min):
            qset = qset.filter(dep_time__gte=datetime_min)
        if is_valid(datetime_max):
            qset = qset.filter(arr_time__lte=datetime_max)
        if is_valid(airline):
            qset = qset.filter(airline__exact=airline)
        if is_valid(dep_ap) and is_valid(arr_ap):
            qset = qset.filter(dep_airport__city__iexact=dep_ap)
            qset = qset.filter(arr_airport__city__iexact=arr_ap)

        return render(request, "flight/flight_form.html", {'queryset': qset, 'a_ch': al_list, 'len': len(qset)})
