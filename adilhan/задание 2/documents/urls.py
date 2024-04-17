from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('register/', views.register, name='register'),
                  path('login/', views.loginPage, name='login'),
                  path('logout/', views.logoutUser, name='logout'),

                  path('documents/', views.document_list, name='document_list'),
                  path('upload/', views.upload_document, name='upload_document'),
                  path('delete/<int:pk>/', views.delete_document, name='delete_document'),
                  path('edit/<int:pk>/', views.edit_document, name='edit_document'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
