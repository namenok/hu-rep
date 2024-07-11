from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'huapp/index.html')


def home(request):
    return render(request, 'huapp/home.html')


def checkme(request):
    return render(request, 'huapp/checkme.html')
