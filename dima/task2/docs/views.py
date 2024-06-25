from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.shortcuts import get_object_or_404

from .models import FileDescription
from .forms import FileDescriptionForm, FileUpdateForm


class FileListView(ListView):
    """
    Получение списка документов
    """
    model = FileDescription
    template_name = 'file_list.html'
    context_object_name = 'files'


class FileDetailView(DetailView):
    """
    Получение данных конкретного документа
    """
    model = FileDescription
    template_name = 'file_detail.html'


class FileCreateView(CreateView):
    """
    Создание документа
    """
    model = FileDescription
    form_class = FileDescriptionForm
    template_name = 'file_form_create.html'
    success_url = reverse_lazy('file_list')


class FileUpdateView(FormView):
    """
    Обновление документа
    """
    form_class = FileUpdateForm
    template_name = 'file_form_update.html'
    success_url = reverse_lazy('file_list')

    def get_initial(self):
        file_instance = get_object_or_404(FileDescription, pk=self.kwargs['pk'])

        initial_data = {
            'description': file_instance.description,
            'title': file_instance.filename()
        }

        return initial_data

    def form_valid(self, form):
        file_instance = get_object_or_404(FileDescription, pk=self.kwargs['pk'])
        file_instance.description = form.cleaned_data['description']
        new_filename = form.cleaned_data['title']

        # Проверка наличие нового имени и на совпадение с прошлым именем
        if new_filename and new_filename != file_instance.filename():
            try:
                file_instance.rename_file(new_filename)
            except FileExistsError:
                return self.render_to_response(self.get_context_data(form=form, error_message="Файл с таким именем уже существует"))

        file_instance.save()
        return super().form_valid(form)


class FileDeleteView(DeleteView):
    """
    Удаление документа
    """
    model = FileDescription
    template_name = 'file_confirm_delete.html'
    success_url = reverse_lazy('file_list')

    def delete(self, *args, **kwargs):
        # Удаление файла из системы
        self.get_object().file.delete()
        return super().delete(*args, **kwargs)
