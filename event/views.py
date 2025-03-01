from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import Events, Myevent
from .forms import NewItemForm


def actual_events(request):

    new_events = Events.objects.order_by('-event_datetime')

    return render(request, 'event/main_page.html', {'new_events': new_events})


@user_passes_test(lambda u: u.is_superuser)
def create_event(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('/')

    else:
        form = NewItemForm()

    return render(request, 'event/new.html', context={'form': form})


@user_passes_test(lambda u: u.is_superuser)
def my_admin_event(request):
    events = Events.objects.filter(user=request.user)
    return render(request, 'event/my_admin_events.html', {'events': events})


@login_required
def add_event(request, pk):
    event = get_object_or_404(Events, pk=pk)
    cart_item, created = Myevent.objects.get_or_create(
        user=request.user,
        event=event
    )

    cart_item.save()

    return redirect('/')

@login_required
def my_user_event(request):
    events = Myevent.objects.filter(user=request.user)

    return render(request, 'event/my_user_events.html', {
        'Myevents': events,
    })


def info_event(request, pk):
    event = get_object_or_404(Events, pk=pk)

    return render(request, 'event/event_detail.html', {'event': event})