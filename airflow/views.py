from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.db import transaction
# Create your views here.


def is_valid(t):
    return t != '' and t is not None


def flight_show(request):
    query_set = Flight.objects.all()
    al_list = list(set(['']+[str(t.airline) for t in query_set]))
    dep_ap = request.GET.get('dep_ap')
    arr_ap = request.GET.get('arr_ap')
    datetime_min = request.GET.get('datetime_min')
    datetime_max = request.GET.get('datetime_max')
    airline = request.GET.get('airline')

    if is_valid(datetime_min):
        query_set = query_set.filter(dep_time__gte=datetime_min)

    if is_valid(datetime_max):
        query_set = query_set.filter(arr_time__lte=datetime_max)

    if is_valid(airline):
        query_set = query_set.filter(airline__exact=airline)

    if is_valid(dep_ap) and is_valid(arr_ap):
        query_set = query_set.filter(dep_airport__city__iexact=dep_ap)
        query_set = query_set.filter(arr_airport__city__iexact=arr_ap)

    return render(request, "flight/flight_form.html", {'queryset': query_set, 'a_ch': al_list, 'len': len(query_set)})


def book_flight(request, flight_id):
    fl = Flight.objects.get(id=flight_id)

    if request.method == 'POST':
        with transaction.atomic():
            cur = Flight.objects.get(id=flight_id)
            required_seats = int(request.POST['seat_count'])
            occupied_seats = 0

            for t in Booking.objects.filter(fl_id=flight_id):
                occupied_seats += int(t.seat_n)

            if occupied_seats + required_seats > cur.aircraft.seats:
                messages.info(request, 'only '+str(cur.aircraft.seats - occupied_seats)+' seat(s) are remaining')
                return render(request, "booking/booking.html", {'flight': fl})

            else:
                messages.info(request, 'Successfully booked')
                Booking.objects.create(user=request.user, fl_id=fl, seat_n=required_seats, total_fare=fl.fare*required_seats).save()
                return redirect('/flights')

    else:
        return render(request, "booking/booking.html", {'flight': fl})


def my_bookings(request):
    book_list = Booking.objects.filter(user=request.user)

    return render(request, "booking/mybooks.html", {'bookset': book_list, 'len': len(book_list)})