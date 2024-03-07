"""
URL configuration for task2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from docs.views import logout_view, main_pageView, AboutMeView, RegisterView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    # Переход к админ панели, стоит по умолчанию
    path('docs/', include('docs.urls')),    # Переход к папке с ссылками в приложении
    path(                                   # Переход на логин страницу
        'login/',
         LoginView.as_view(
             template_name='login.html',
            redirect_authenticated_user=True,
         ),
         name='login'),
    path('', main_pageView.as_view(), name='main'),    # Главная страница
    path('logout/', logout_view, name='logout'),       # Ссылка для выхода из сессии, страницы у нее нет
    path('about-me/', AboutMeView.as_view(), name='about-me'),      # Ссылка для страницы-информации о сессии
    path('register/', RegisterView.as_view(), name='register')      # Ссылка для регистрации

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # Добавили для работы с файлами
