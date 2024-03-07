from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='media/')

    class Meta:
        db_table = 'document'
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
