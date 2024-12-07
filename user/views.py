from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the user interface ...")

def base1(request):
    return render(request,'base1.html')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Correct way to log the user in
            return redirect('/')  # Redirect to a base page or another page after login
        else:
            return HttpResponse("Invalid login credentials")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set the user's password correctly
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



