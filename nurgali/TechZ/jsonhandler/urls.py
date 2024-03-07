from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_json, name='upload_json'),
    path('success-view', views.success_view, name='success_view')
]
