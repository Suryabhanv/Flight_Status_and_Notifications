
# Create your views here.
from django.shortcuts import render
from .models import Flight

def flight_status(request):
    flights = Flight.objects.all()
    return render(request, 'core/flight_status.html', {'flights': flights})
