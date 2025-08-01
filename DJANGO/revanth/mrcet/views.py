from django.shortcuts import render,redirect
from .models import student

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout

# Create your views here.

def contact (request):
    c = student.objects.all()
    return render(request, 'contact.html', {'dsa': c})

def details(request, slug):
    csd = student.objects.get(slug=slug)
    return render(request, 'details.html', {'Csd': csd})


def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("contact")
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('contact')
    return render(request, 'logout.html')                    


