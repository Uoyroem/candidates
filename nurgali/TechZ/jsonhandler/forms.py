from django import forms
from django.core.exceptions import ValidationError


class JSONImportForm(forms.Form):
    json_file = forms.FileField(label='Выберите JSON файл')

    def clean_json_file(self):
        file = self.cleaned_data['json_file']
        if not file.name.endswith('.json'):
            raise ValidationError('Неверный тип файла. Требуется файл с расширением .json.')
        return file