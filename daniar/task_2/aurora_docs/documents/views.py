from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm


@login_required(login_url='/login/')
def document_list(request):
    """
    Отображает список всех документов.
    """
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})


@login_required(login_url='/login/')
def upload_document(request):
    """
    Загружает новый документ.
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(user=request.user)
    return render(request, 'documents/upload_document.html', {'form': form})


@login_required(login_url='/login/')
@permission_required('documents.update_document', login_url='/no_permission/')
def update_document(request, pk):
    """
    Обновляет существующий документ.
    """
    doc = Document.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            form.save()
            return redirect('document_list')
        else:
            print(f'FORM ERRORS - {form.errors}')
    else:
        form = DocumentForm(instance=doc)
    return render(request, 'documents/document.html', {'form': form})


@login_required(login_url='/login/')
@permission_required('documents.update_document', login_url='/no_permission/')
def get_document(request, pk):
    """
    Получает существующий документ.
    """
    doc = Document.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=doc)
    return render(request, 'documents/document.html', {'form': form})


@permission_required('documents.delete_document', login_url='/no_permission/')
def delete_document(request, pk):
    """
    Удаляет существующий документ.
    """
    doc = Document.objects.get(pk=pk)
    doc.delete()
    return redirect('document_list')


def login_view(request):
    """
    Обрабатывает вход пользователя.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('document_list')
        else:
            print(f'FORM ERRORS - {form.errors}')
    else:
        form = AuthenticationForm()
    return render(request, 'documents/login.html', {'form': form})


def logout_view(request):
    """
    Обрабатывает выход пользователя.
    """
    logout(request)
    return redirect('document_list')


def no_permission(request):
    """
    Обрабатывает случаи, когда у пользователя нет необходимых разрешений.
    """
    return render(request, 'documents/no_permission.html')
