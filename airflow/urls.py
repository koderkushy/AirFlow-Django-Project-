from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.flight_show, name='flight_show'),
]
