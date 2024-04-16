from django.shortcuts import render, get_object_or_404

from .models import Flight

def detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    return render(request, 'flight/detail.html', {
        'flight': flight
    })