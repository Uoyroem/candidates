from django.contrib import admin
from .models import Document, Counteragent, Responsible

admin.site.register(Document)
admin.site.register(Counteragent)
admin.site.register(Responsible)

