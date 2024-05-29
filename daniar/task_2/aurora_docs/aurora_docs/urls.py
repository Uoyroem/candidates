from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from documents import views as doc_views

urlpatterns = [
    path('', doc_views.document_list, name='document_list'),
    path('admin/', admin.site.urls),
    path('documents/', include('documents.urls')),
    path('documents/upload/', doc_views.upload_document, name='upload_document'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', doc_views.login_view, name='login'),
    path('logout/', doc_views.logout_view, name='logout'),
    path('no_permission/', doc_views.no_permission, name='no_permission'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
