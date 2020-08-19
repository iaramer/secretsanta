from django.shortcuts import render


def home(request):
    return render(request, 'core/homePage.html')


def welcome(request):
    return render(request, 'core/homePage.html')


def signup(request):
    return render(request, 'core/homePage.html')


def login(request):
    return render(request, 'core/homePage.html')


def party(request):
    return render(request, 'core/homePage.html')
