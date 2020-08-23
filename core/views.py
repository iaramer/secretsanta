from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    return render(request, 'core/homePage.html')


def welcome(request):
    return render(request, 'core/homePage.html')


def signup(request):
    users = User.objects.all()

    if request.method == 'POST':
        username = request.POST.get('uname')
        first_name = request.POST.get('fname')
        second_name = request.POST.get('sname')
        email = request.POST.get('eml')
        password = request.POST.get('pwd')
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=second_name)
        user.save()

        request.method = 'GET'

    return render(request, 'core/signup.html', {'users': users})


def login(request):
    return render(request, 'core/login.html')


def party(request):
    return render(request, 'core/homePage.html')
