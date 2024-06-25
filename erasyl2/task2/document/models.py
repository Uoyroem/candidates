from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Document(models.Model):
    """
    Модель файла документа, у которого есть юзер, название, описание,
    сам файл(место где хранится) и дата загрузки
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title




