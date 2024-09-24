from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'home.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confrim-password')

        print(password, confirm_password)
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('register')

        
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        print(
            f'User {user.username} created'
        )
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    
    return render(request, 'registration.html')

