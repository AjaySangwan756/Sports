from django.shortcuts import render, redirect
from .models import Player, Event, Plan, SportsSchedule

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

def schedule(request):
    if request.method == 'POST':
        command = request.POST['command']
        type = request.POST['type']
        print(command)
        Plan.objects.create(command=command, type=type)
        return redirect('plan')
    return render(request, 'schedule.html')

def plan(request):
    if request.method == 'POST':
        sports = request.POST['sports']
        year = request.POST['year']
        period_from = request.POST['period_from']
        period_to = request.POST['period_to']
        SportsSchedule.objects.create(sports=sports, year=year, period_from=period_from, period_to=period_to)
        return redirect('dashboard')
    return render(request, 'plan.html')

def dashboard(request):
    plan=Plan.objects.all()
    for n in plan:
        print(n.command)
        print(n.type)
        if n.command=='Central_Command':
            if n.type=='Inter_Battallion':
                print('Yes')
        else:
            print('No')
    print(plan)
    schedule=SportsSchedule.objects.all()
    print(schedule)
    return render(request, 'dashboard.html', {'plan':plan})