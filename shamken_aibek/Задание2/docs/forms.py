from django import forms
from .models import DocumentModel


# Создаем класс, который наследуем из models.py.
class Documents(forms.ModelForm):
    class Meta:
        model = DocumentModel
        exclude = ['author', 'archived']  # Убираем два поля
        # Первый убрали потому что автора будем получать автоматически из сессии
        # Второе, чтобы мог делать только superUser в админ панели

