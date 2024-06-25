from django import forms
from .models import FileDescription


class FileDescriptionForm(forms.ModelForm):
    class Meta:
        model = FileDescription
        fields = ['description', 'file']


class FileUpdateForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = forms.CharField()
