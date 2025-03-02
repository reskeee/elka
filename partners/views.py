from django.shortcuts import render, redirect, get_object_or_404
from .forms import PartnersForm, PartnersImageFormSet
from .models import Partners


def create_partner(request):
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES)
        formset = PartnersImageFormSet(request.POST, request.FILES, instance=Partners())
        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product
            formset.save()
            return redirect('/')
    else:
        form = PartnersForm()
        formset = PartnersImageFormSet(instance=Partners())

    return render(request, 'partners/create_partners.html', {'form': form, 'formset': formset})


def partners(request):
    partners = Partners.objects.all()

    return render(request, 'partners/partners.html', {'partners': partners})


def info_partner(request, pk):
    partner = get_object_or_404(Partners, pk=pk)

    return render(request, 'partners/detail_partner.html', context={'partner': partner})