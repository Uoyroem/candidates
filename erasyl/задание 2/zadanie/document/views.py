from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Document


# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['uploaded_file']:
        uploaded_file = request.FILES['uploaded_file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        filename = fs.url(filename)
        return render(request, 'home.html', {
            'filename': filename
        })
    else:
        return render(request, 'home.html', {})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        if password1 == password2:
            User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
        user = authenticate(username=username, password=password1)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')


@csrf_exempt
def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')