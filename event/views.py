from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import Events
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