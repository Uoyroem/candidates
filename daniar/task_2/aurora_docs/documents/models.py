from django.conf import settings
from django.db import models


class Document(models.Model):
    """
    Document - это модель, которая представляет документ в системе.

    Она включает в себя следующие поля:
    - title: заголовок документа
    - description: описание документа
    - file: файл документа
    - uploaded_at: дата и время загрузки документа
    - user: пользователь, который загрузил документ
    """

    title = models.CharField(max_length=35, blank=False, null=False)
    description = models.TextField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to='documents/', blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """
        Возвращает строковое представление модели, которое используется Django в различных местах, например, в административном интерфейсе.
        """
        return self.title
