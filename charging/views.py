from django.shortcuts import render
from .models import Station

def home(request):
    stations = Station.objects.all()
    return render(request, 'home.html', {'stations': stations})
from .models import Station, Booking
from django.shortcuts import render, redirect

def book_station(request):
    if request.method == 'POST':
        name = request.POST['name']
        station_id = request.POST['station']
        units = float(request.POST['units'])

        station = Station.objects.get(id=station_id)

        cost = units * station.rate

        Booking.objects.create(
            customer_name=name,
            station=station,
            units=units,
            total_cost=cost
        )

        # Reduce slot count
        station.slots -= 1
        station.save()

    stations = Station.objects.all()
    return render(request, 'booking.html', {'stations': stations})
        

    return redirect('bookings')

    stations = Station.objects.all()
    return render(request, 'booking.html', {'stations': stations})
def bookings(request):
    booking_data = Booking.objects.all()

    return render(
        request,
        'bookings.html',
        {'bookings': booking_data}
    )
    return render(request, 'booking.html', {
    'stations': stations,
    'cost': cost
})