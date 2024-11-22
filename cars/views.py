from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)
        #cars = Car.objects.filter(model__contains='chevro')
    
    return render(request, 'cars.html', {'cars': cars})