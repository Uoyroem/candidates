from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import DocumentModel


@admin.action(description='Archive documents')
def mark_archived(modeladmin: admin.ModelAdmin, request:HttpRequest, queryset:QuerySet):
    queryset.update(archived=True)


@admin.action(description='Unarchive documents')
def mark_unarchived(modeladmin: admin.ModelAdmin, request:HttpRequest, queryset:QuerySet):
    queryset.update(archived=False)


@admin.register(DocumentModel)
class DocumentAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
    ]
    list_display = ('pk', 'name', 'author_verbose', 'description_short', 'created_at', 'file', 'archived')
    list_display_links = 'pk', 'name', 'author_verbose',
    search_fields = ('name', 'description', 'created_at')

    def get_queryset(self, request):
        return DocumentModel.objects.select_related('author')



#
# admin.site.register(DocumentModel, DocumentAdmin)

# Register your models here.
