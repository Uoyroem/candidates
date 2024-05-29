from django import forms
from .models import Document
from django.contrib.auth import get_user_model

User = get_user_model()


class DocumentForm(forms.ModelForm):
    """
    DocumentForm - это форма для создания и обновления экземпляров Document.

    Она включает в себя четыре поля: 'title', 'description', 'file' и 'user'.
    Поле 'user' отключено и автоматически заполняется текущим пользователем.
    """

    # Поле 'user' отключено, так как оно будет автоматически заполняться текущим пользователем
    user = forms.CharField(disabled=True)

    # Поле 'title' - это текстовое поле ввода с подсказкой
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Название'}))

    # Поле 'description' - это поле textarea с подсказкой
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Описание'}))

    class Meta:
        model = Document
        fields = ['title', 'description', 'file', 'user']

    def __init__(self, *args, user=None, **kwargs):
        """
        Инициализация формы.

        Если предоставлен пользователь, поле 'user' заполняется именем предоставленного пользователя.
        """
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user
            self.fields['user'].initial = user.username

    def clean_user(self):
        """
        Проверка поля 'user'.

        Если предоставленное значение является цифрой, оно рассматривается как ID пользователя.
        В противном случае оно рассматривается как имя пользователя.
        Если пользователь с предоставленным ID или именем пользователя не существует, возникает ошибка проверки.
        """
        user_id_or_username = self.cleaned_data.get('user')
        try:
            if user_id_or_username.isdigit():
                user = User.objects.get(pk=user_id_or_username)
            else:
                user = User.objects.get(username=user_id_or_username)
        except User.DoesNotExist:
            raise forms.ValidationError("Пользователь с ID или именем пользователя %s не существует." % user_id_or_username)
        return user
