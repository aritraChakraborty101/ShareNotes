from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')
    
    context = {}

    return render(request, 'login.html', context)


def register(request):
    return render(request, 'registration.html')

