import random

from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Event


class MainView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'index.html', context={'events': events})


class EventDetailsView(View):
    def get(self, request, *args, **kwargs):
        event_id = kwargs['pk']
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'detail.html', context={'event': event})
