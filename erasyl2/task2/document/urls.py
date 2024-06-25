from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.document_list, name='list'),
    path('register/', views.register, name='register'),
    path('create/', views.document_create, name='create'), # добавление документа
    path('detail/<int:id>/', views.document_detail, name='detail'), # чтение документа
    path('edit/<int:id>/', views.document_edit, name='edit'), # обновление документа
    path('delete/<int:id>/', views.document_delete, name='delete'), # удаление документа
]