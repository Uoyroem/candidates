from django.contrib import admin
from .models import Document

# Register your models here.


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'file', 'uploaded_at']
    search_fields = ['title']