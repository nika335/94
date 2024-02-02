from django.shortcuts import render, redirect
from .models import Events
from django.http import HttpResponseNotFound


def index(request):
    enents = Events.objects.all()
    return render(request, 'index.html', {'events':enents})


def event_detals(request, TITLE):
    try:
        events = Events.objects.get(title=TITLE)
        return render(request, 'event_detals.html', {'events':events})
    except Events.DoesNotExist:
        return HttpResponseNotFound('The requested object does not exist.')



def add_events(request):
    if request.method == 'POST':
        new_event = Events(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            date = request.POST.get('date'),
            location = request.POST.get('location'),
        )
        new_event.save()
        return redirect('index')
    return render(request, 'new_event.html')