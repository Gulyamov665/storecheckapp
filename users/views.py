from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from users.forms import SignUpForm, SignInForm
from django.contrib.auth.forms import AuthenticationForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:sign_in')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store:home')
    form = AuthenticationForm()
    return render(request, 'sign_in1.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')
