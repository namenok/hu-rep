from django.shortcuts import render, redirect, get_object_or_404

from .forms import EntryForm, FotoForm
from django.contrib.auth.decorators import login_required
from .models import Category, Post, LibText, Teg

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse





def get_categories():
    all = Category.objects.all()
    count = all.count()

    return {
        "cat1":all[:count//2],
        "cat2":all[count//2:]
    }


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
    post_blog_list = Post.objects.all().order_by("-published_date")
    # id_post_blog_list = Post.objects.get(pk=1) #просто перевірили фільтр
    my_posts_list = LibText.objects.all()
    # category_list = Category.objects.all()

    tegs = Teg.objects.all()

    context = {"post_blog_list": post_blog_list,
               "my_posts_list": my_posts_list,
               # "category_list": category_list,
               # "post": id_post_blog_list,
               "tegs": tegs}
    context.update(get_categories())

    return render(request, 'huapp/library.html', context=context)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    context={"post": post}
    context.update(get_categories())
    return  render(request, 'huapp/post.html', context=context)


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




def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c)
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'huapp/library.html', context=context)