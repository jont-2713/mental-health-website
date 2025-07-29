from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.success(request, "Error logging in. Try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def registerUser(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered.")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {"form": form})
        
    return render(request, 'register.html', {"form": form})

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully been logged out.")
    return redirect('login')