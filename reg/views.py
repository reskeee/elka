from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/login/')
    else:
        form = SignupForm()
    return render(request, 'reg/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
