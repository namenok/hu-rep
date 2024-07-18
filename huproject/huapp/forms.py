from django import forms

from .models import HomeInfo


class HomeInfoForm(forms.ModelForm):
    class Meta:
        model = HomeInfo
        fields = ['text', 'img', ]
        labels = {'text': 'test text', 'img': 'test img'}
