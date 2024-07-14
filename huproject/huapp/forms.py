from django import forms
from .models import TeachertData, StudentData


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeachertData
        fields = "__all__"
