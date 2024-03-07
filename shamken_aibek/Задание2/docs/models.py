from django.db import models
from django.contrib.auth.models import User


# Создаем модель, для документов которые будем создавать изменять и т.д.
class DocumentModel(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='', null=False)       # Будем добавлять сам файл
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)  # Автора будем указывать из сессии
    archived = models.BooleanField(default=False)    # Флаг, для того чтоб не выводить архивные данные

    @property
    def description_short(self) -> str:     # Для удобного вывода описания документа
        if len(self.description) < 100:
            return self.description
        return self.description[:100] + '...'

    def __str__(self) -> str:               # Для удобного вывода на админ панели
        return f'ID:{self.pk} | Document: {self.name}'

    def author_verbose(self) -> str:        # Для удобного вывода автора документа
        if f'{self.author.first_name} {self.author.last_name}' == ' ':
            return self.author.username
        return f'{self.author.first_name} {self.author.last_name}'
