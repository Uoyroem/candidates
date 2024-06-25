from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from .models import Document
from .forms import DocumentForm, UserRegisterForm, LoginForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user}
            )
    else:
        form = UserRegisterForm()
    return render(
        request,
        'account/register.html',
        {'form': form}
    )


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                email=cd['email'],
                password=cd['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid email or password')
    else:
        form = LoginForm()
    return render(
        request,
        'registration/login.html',
        {'form': form}
    )

@login_required
def document_list(request):
    documents = Document.objects.all()
    return render(
        request,
        'documents/list.html',
        {'documents': documents}
    )


@login_required
def document_detail(request, id):
    document = get_object_or_404(Document, id=id)
    return render(
        request,
        'documents/detail.html',
        {'document': document}
    )


@login_required
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) # принимаем запросы с файлами
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.user = request.user
            new_file.save()
            return redirect('list')
    else:
        form = DocumentForm()
    return render(
        request,
        'documents/create.html',
        {'form': form}
    )


@login_required
def document_delete(request, id):
    document = Document.objects.get(id=id)
    document.delete()
    return redirect('list')


@login_required
def document_edit(request, id):
    document = get_object_or_404(Document, id=id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('detail', id=document.id)
    else:
        form = DocumentForm(instance=document)
    return render(
        request,
        'documents/edit.html',
        {'form': form}
    )
