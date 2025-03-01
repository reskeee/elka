from django.shortcuts import render

from .models import Events


def actual_events(request):

    new_events = Events.objects.order_by('-event_datetime')[:3]

    active_events = Events.objects.order_by('event_datetime').filter(status='active')[:3]

    return render(request, 'event/main_page.html', {'new_events': new_events,
                                                    'active_events': active_events})