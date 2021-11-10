from django.urls import path
from . import views

urlpatterns = [
    path('airports/', views.fetch_airports, name='airports'),
    path('flights/', views.)
]