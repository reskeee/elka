from calendar import HTMLCalendar
from django.utils import timezone

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import Events, Myevent
from .forms import NewItemForm, EditItemForm


def actual_events(request):

    new_events = Events.objects.order_by('-event_datetime')[:8]

    return render(request, 'event/main_page.html', {'new_events': new_events})


@user_passes_test(lambda u: u.is_superuser)
def create_event(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
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
    myeve = Myevent.objects.filter(user=request.user)

    return render(request, 'event/my_user_events.html', {
        'Myevents': myeve,
    })


def info_event(request, pk):
    event = get_object_or_404(Events, pk=pk)

    return render(request, 'event/event_detail.html', {'event': event})

def all_event(request):
    query = request.GET.get('query', '')
    event = Events.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if query:
        event = event.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if start_date and end_date:
        event = event.filter(event_datetime__range=(start_date, end_date))

    paginator = Paginator(event, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'event/all.html', context={'event': event,
                                                       'query': query,
                                                       'page_obj': page_obj})

@user_passes_test(lambda u: u.is_superuser)
def delete(request, pk):
    event = get_object_or_404(Events, pk=pk)
    event.delete()

    return redirect('/')


def user_calendar(request):
    user = request.user  # Текущий пользователь

    # Получаем год и месяц из запроса
    try:
        year = int(request.GET.get('year', timezone.now().year))
        month = int(request.GET.get('month', timezone.now().month))
    except (ValueError, TypeError):
        year = timezone.now().year
        month = timezone.now().month

    # Корректируем год и месяц, если они некорректны
    if month > 12:
        year += 1
        month = 1
    elif month < 1:
        year -= 1
        month = 12

    # Получаем лайкнутые события пользователя
    my_events = Myevent.objects.filter(user=user).select_related('event')

    # Создаём календарь
    cal = HTMLCalendar().formatmonth(year, month)

    # Формируем данные для отображения событий в календаре
    events_dict = {}
    for my_event in my_events:
        event_date = my_event.event.event_datetime.date()  # Дата события
        if event_date not in events_dict:
            events_dict[event_date] = []
        events_dict[event_date].append(my_event.event)

    return render(request, 'event/user_calendar.html', {
        'calendar': cal,
        'events_dict': events_dict,
        'year': year,
        'month': month,
    })


@user_passes_test(lambda u: u.is_superuser)
def edit(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()

            return redirect('event:info_event', pk=event.id)

    else:
        form = EditItemForm(instance=event)

    return render(request, 'event/edit_event.html', context={'form': form})