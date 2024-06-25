from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda req: redirect('/docs/')),

    path('docs/', include("docs.urls"), name="docs"),
    path('auth/', include("jwt_auth.urls.static"), name="auth"),

    path('api/v1/', include('jwt_auth.urls.api')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
