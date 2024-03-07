from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import Documents
from .models import DocumentModel


# Шаблон, чтобы знать через кого мы зашли, просто для информации
class AboutMeView(TemplateView):
    template_name = 'docs/about-me.html'


# Шаблон регистрации, взял его из готовой библиотеки, но можно было и создать вручную
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'docs/register.html'
    success_url = reverse_lazy('login')


# Шаблон главной страницы
class main_pageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'main.html')


# Функция для выхода из сессии
def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('main'))


# Шаблон главной страницы про документы и для перехода к списку загруженных документов
class docs_indexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        doc_files = {
            ('Word', '.docx'),
            ('Excel', '.xlsx'),
            ('PDF', '.pdf'),
            ('Power Point', '.pptx'),
        }

        context = {
            "doc_files": doc_files,
        }
        return render(request, 'docs/docs-index.html', context=context)


# Шаблон страницы со списком загруженных документов, использовал готовую библиотеку ListView
# Нужны права доступа у пользователя
class docs_listView(PermissionRequiredMixin, ListView):
    permission_required = 'view_documentmodel'
    template_name = 'docs/docs-list.html'
    context_object_name = 'docs'
    queryset = DocumentModel.objects.filter(archived=False).order_by('-created_at')


# Шаблон для загрузки файлов
# Нужны права доступа у пользователя
class create_docsView(PermissionRequiredMixin, View):
    permission_required = 'add_documentmodel'
    def get(self, request):
        form = Documents()
        return render(request, 'docs/create-doc.html', {'docs': form})

    def post(self, request):
        form = Documents(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)      # Сразу не сохраняем, чтобы передать автора
            document.author = request.user       # Передаем автора из аутентифицированного пользователя
            document.save()                     # Теперь сохраняем
            return redirect(reverse('docs:docs_list'))
        return render(request, 'docs/create-doc.html', {'docs': form})


# Шаблон, чтобы обновить информацию про документ
# Нужны права доступа
class docs_updateView(PermissionRequiredMixin, View):
    permission_required = 'change_documentmodel'

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        # Получаем объект по его pk, или возвращаем 404, если такого объекта нет
        document = get_object_or_404(DocumentModel, pk=pk)
        # Создаем форму для объекта и заполняем ее текущими данными
        form = Documents(instance=document)
        context = {
            'form': form,
            'docs': document

        }
        return render(request, 'docs/update-doc.html', context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        # Снова получаем объект
        document = get_object_or_404(DocumentModel, pk=pk)
        # Создаем форму с данными из запроса и файлами
        form = Documents(request.POST, request.FILES, instance=document)
        if form.is_valid():
            # Сохраняем обновленные данные
            form.save()
            # Перенаправляем пользователя на страницу списка документов
            return redirect(reverse('docs:docs_list'))
        # Если форма не валидна, возвращаем пользователя на страницу формы с указанием ошибок
        return render(request, 'docs/update-doc.html', {'form': form, 'document': document})


# Шаблон подробной информации про документ
# Нужны права доступа
class docs_detailView(PermissionRequiredMixin, DetailView):
    permission_required = 'view_documentmodel'
    template_name = 'docs/docs-detail.html'
    queryset = DocumentModel.objects.filter(archived=False)
    context_object_name = 'doc'


# Хочу показать что умею пользоваться cookies, но не особо понимаю для чего их лучше использовать
def set_cookieView(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response

def get_cookieView(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz', 'default value')
    return HttpResponse('Cookie value '+value)


def set_sessionView(request: HttpRequest) -> HttpResponse:
    request.session['foobar'] = 'spameggs'
    return HttpResponse('Session set')


def get_sessionView(request: HttpRequest) -> HttpResponse:
    value = request.session.get('foobar', 'default value')
    return HttpResponse('Session value: '+value)


# Тут будут 2 шаблона для информационных страниц, куда не нужны права доступа
class about_pageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'docs/about.html')

class question_pageView(View):
    def get(self, request:HttpRequest) -> HttpResponse:
        return render(request, 'docs/questions.html')


# Как вариант можно было бы использовать свой шаблон для логина
# Где можно легко поставить проверку через email

# def login_view(request: HttpRequest):
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect("/admin/")
#         return render(request, "login.html")
#     username = request.POST["username"]
#     password = request.POST["password"]
#
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("/admin/")
#
#     return render(request, "login.html", {'error': 'Invalid username or password'})
#
