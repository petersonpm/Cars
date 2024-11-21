from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.filter(model__contains='che')
    
    return render(request, 'cars.html', {'cars': cars})