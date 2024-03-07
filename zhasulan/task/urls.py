from django.urls import path
from .views import import_data, table_view

urlpatterns = [
    path('import/', import_data, name='import_data'),
    path('table/', table_view, name='table_view'),
]
