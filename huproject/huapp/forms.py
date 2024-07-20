from django import forms

from .models import HomeInfo

from .models import GeeksModel


class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"


class HomeInfoForm(forms.ModelForm):
    class Meta:
        model = HomeInfo
        fields = ['text', 'img', ]
        labels = {'text': 'text', 'img': 'img'}

