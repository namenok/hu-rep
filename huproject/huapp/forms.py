from django import forms

from .models import Entry, Foto


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', ]
        labels = {'text': 'Entry text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['image']

