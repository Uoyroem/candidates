import os
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class Document(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='documents/templates/files')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('document_detail', args=[str(self.id)])

@receiver(post_delete, sender=Document)
def delete_document_file(sender, instance, **kwargs):
    # Delete the associated PDF file when the Document object is deleted
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

post_delete.connect(delete_document_file, sender=Document)


@receiver(pre_save, sender=Document)
def delete_old_document_file(sender, instance, **kwargs):
    # Check if the Document object being updated has an existing file
    if instance.pk:
        try:
            old_file = Document.objects.get(pk=instance.pk).file
        except Document.DoesNotExist:
            return
        if old_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)





class Auth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None