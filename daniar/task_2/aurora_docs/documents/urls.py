from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('delete/<int:pk>/', views.delete_document, name='delete_document'),
    path('documents/<int:pk>/edit/', views.update_document, name='update_document'),

]
