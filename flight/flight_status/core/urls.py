from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_status, name='flight_status'),
    # Add other URL patterns here
]
