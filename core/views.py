from django.shortcuts import render

from core.models import User


def home(request):
    return render(request, 'core/homePage.html')


def welcome(request):
    return render(request, 'core/homePage.html')


def signup(request):
    users = User.objects.all()

    if request.method == 'POST':
        user = User()
        user.first_name = request.POST.get('fname')
        user.second_name = request.POST.get('sname')
        user.email = request.POST.get('eml')
        user.password = request.POST.get('pwd')
        user.save()

        request.method = 'GET'

    return render(request, 'core/signup.html', {'users': users})


def login(request):
    return render(request, 'core/login.html')


def party(request):
    return render(request, 'core/homePage.html')
