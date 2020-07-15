from django.shortcuts import render
from django.http import HttpResponse


# todo: temporary method, remove after a while
def test_response(request):
    return HttpResponse("<h3>Starting Secret Santa party!</h3>")


def index(request):
    return render(request, 'parties/homePage.html')
