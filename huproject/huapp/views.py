

from django.shortcuts import render, redirect

from .forms import EntryForm
from django.contrib.auth.decorators import login_required


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from .forms import FotoForm


@login_required()
def image_upload(request):

    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect('huapp:home')
    else:
        form = FotoForm()
    return render(request, 'huapp/image_uploads.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')


def index(request):
    return render(request, 'huapp/index.html')


@login_required()
def home(request):

    # тимчасовий приклад
    lst = ['one', 'two', 'three']
    title = "Вітаю!"
    context = {
        "title":title,
        "list_data": lst,
    }


    return render(request, 'huapp/home.html', context=context)


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
def new_entry(request):

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return redirect('huapp:home')

    context = {'form': form}
    return render(
        request,
        'huapp/new_entry.html',
        context=context)


