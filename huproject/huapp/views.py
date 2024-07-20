from django.shortcuts import render, redirect
from django.http import Http404
from .forms import HomeInfoForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'huapp/index.html')


@login_required()
def home(request):
    return render(request, 'huapp/home.html')


@login_required()
def checkme(request):
    return render(request, 'huapp/checkme.html')


@login_required()
def library(request):
    return render(request, 'huapp/library.html')


@login_required()
def calendar(request):
    return render(request, 'huapp/calendar.html')


@login_required()
def home_test_form(request):

    if request.method != 'POST':
        form = HomeInfoForm()
    else:
        form = HomeInfoForm(request.POST)
        if form.is_valid():
            new_forminfo = form.save(commit=False)
            new_forminfo.owner = request.user
            new_forminfo.save()
            return redirect('huapp:home')

    context = {'form': form}
    return render(
        request,
        'huapp/home_test_form.html',
        context=context
    )