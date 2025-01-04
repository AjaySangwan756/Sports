from django.shortcuts import render, redirect
from .models import Player, Event

def dashboard(request):
    players = Player.objects.all()
    events = Event.objects.all()
    return render(request, 'dashboard.html', {'players': players, 'events': events})

def add_player(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        Player.objects.create(name=name, email=email, age=age)
        return redirect('dashboard')
    return render(request, 'add_player.html')

def add_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        location = request.POST['location']
        event = Event.objects.create(title=title, date=date, location=location)
        return redirect('dashboard')
    return render(request, 'add_event.html')
