from django.shortcuts import render, redirect

from flight.models import Flight

from .forms import SignupForm

def index(request):
    flights = Flight.objects.all()
    return render(request, 'core/index.html',{
        'flights': flights,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form = SignupForm

    return render(request, 'core/signup.html',{
        'form': form
    })