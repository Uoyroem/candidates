from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()
    class Meta:
        model = get_user_model()
        fields = ('email', 'username','password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user