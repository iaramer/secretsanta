from django.contrib.auth.models import User
from django.shortcuts import render
from core.form import SignUpForm


def home(request):
    return render(request, 'core/homePage.html')


def welcome(request):
    return render(request, 'core/homePage.html')


def signup(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

        request.method = 'GET'
        return render(request, 'core/signup.html', {'form': form, 'users': users})
    else:
        form = SignUpForm()
        return render(request, 'core/signup.html', {'form': form, 'users': users})


def login(request):
    return render(request, 'core/login.html')


def party(request):
    return render(request, 'core/homePage.html')
