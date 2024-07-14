from django.shortcuts import render, redirect

from .forms import StudentForm, TeacherForm
from django.views.generic.list import ListView
from django.urls import reverse
from multi_form_view import MultiModelFormView


def index(request):
    return render(request, 'huapp/index.html')



# https://www.tutorialspoint.com/django-handling-multiple-forms-in-single-view
class SchoolData(MultiModelFormView):
    form_classes = {
        'student_form': StudentForm,
        'teacher_form': TeacherForm,
    }
    template_name = 'home.html'

    def get_success_url(self):
        return reverse('home')

    def forms_valid(self, forms):
        student = forms['student_form'].save(commit=False)
        teacher = forms['teacher_form'].save(commit=False)
        return super(SchoolData, self).forms_valid(forms)


def checkme(request):
    return render(request, 'huapp/checkme.html')


def library(request):
    return render(request, 'huapp/library.html')


def calendar(request):
    return render(request, 'huapp/calendar.html')
