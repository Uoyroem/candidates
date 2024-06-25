import os

from django.db import models


class FileDescription(models.Model):
    description = models.TextField()
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title
    
    def filename(self):
        """
        Имя файла без пути
        """
        return os.path.basename(self.file.name)
    
    def rename_file(self, new_name):
        """
        Переименование файла в системе
        """
        old_path = self.file.path
        new_path = os.path.join(os.path.dirname(old_path), new_name)

        os.rename(old_path, new_path)

        self.file.name = os.path.join('files', new_name)
        self.save()
