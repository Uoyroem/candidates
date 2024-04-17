from rest_framework import generics
from .models import Document
from django.shortcuts import render, get_object_or_404
from .serializers import DocumentSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .serializers import DocumentSerializer
from .forms import UserForm
from rest_framework.response import Response

class DocumentListCreate(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'documents/document_details.html', {'document': document})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'documents/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'documents/login.html')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL
    else:
        form = UserCreationForm()
    return render(request, 'documents/register.html', {'form': form})

