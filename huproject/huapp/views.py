from django.shortcuts import render, redirect
from django.http import Http404
from .forms import HomeInfoForm, GeeksForm
from django.contrib.auth.decorators import login_required


@login_required()
def home_view(request):
    form = GeeksForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'huapp/geeks.html', context=context)



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
            new_form_info = form.save(commit=False)
            new_form_info.owner = request.user
            new_form_info.save()
            return redirect('huapp:home')

    context = {'form': form}
    return render(
        request,
        'huapp/home_test_form.html',
        context=context
    )