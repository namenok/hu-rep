from django.shortcuts import render, redirect

from .forms import EntryForm
from django.contrib.auth.decorators import login_required


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render


def image_upload(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()

        # save the image on MEDIA_ROOT folder
        file_name = fs.save(image.name, image)

        # get file url with respect to `MEDIA_URL`
        file_url = fs.url(file_name)
        return HttpResponse(file_url)
    else:
        # render the form
        return render(request, "image_uploads.html")








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


