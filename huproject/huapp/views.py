from django.shortcuts import render, redirect
from .forms import HomeInfoForm


def index(request):
    return render(request, 'huapp/index.html')


def home(request):
    return render(request, 'huapp/home.html')


def checkme(request):
    return render(request, 'huapp/checkme.html')


def library(request):
    return render(request, 'huapp/library.html')


def calendar(request):
    return render(request, 'huapp/calendar.html')


def test_form(request):
    if request.method != 'POST':
        form = HomeInfoForm()
    else:
        form = HomeInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('huapp:home')

    context = {'form': form}
    return render(
        request,
        'huapp/home_test_form.html',
        context=context
    )