from django.forms import *
from .models import *


class FlightRegister(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'


class FlightFilter(Form):
    dep_ap = CharField(label='Departure', max_length=20)
    arr_ap = CharField(label='Arrival', max_length=20)
    dtime_min = DateTimeField(label='Least Departure Time')
    dtime_max = DateTimeField(label='Maximum Arrival Time')
    Aline = CharField(label='Airliner', max_length=20)
