from django.urls import path
from .views import FileListView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView

urlpatterns = [
    path('', FileListView.as_view(), name='file_list'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/new/', FileCreateView.as_view(), name='file_create'),
    path('file/<int:pk>/edit/', FileUpdateView.as_view(), name='file_update'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),
]
