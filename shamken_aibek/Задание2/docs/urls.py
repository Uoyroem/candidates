from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import (docs_indexView,
                    docs_listView,
                    create_docsView,
                    docs_detailView,
                    docs_updateView,
                    about_pageView,
                    question_pageView,
                    get_cookieView,
                    set_cookieView,
                    set_sessionView,
                    get_sessionView,
                    )
# Тут будут ссылки и функции или классы как отображать страницы
# Так же добавил им имя, чтобы можно было указать не путь, который может поменяться, а типа id ссылки
app_name = 'docs'
urlpatterns = [
    path('', docs_indexView.as_view(), name='index'),
    path('list/', docs_listView.as_view(), name='docs_list'),
    path('create/', create_docsView.as_view(), name='create_document'),
    path('list/<int:pk>/', docs_detailView.as_view(), name='docs_detail'),         # Для того чтобы выводить конкретный файл
    path('list/<int:pk>/update/', docs_updateView.as_view(), name='docs_update'),  # Для того чтобы изменить конкретный файл
    path('about/', about_pageView.as_view(), name='about'),
    path('questions/', question_pageView.as_view(), name='questions'),
    path('get_cookie/', get_cookieView, name='get_cookie'),
    path('set_cookie/', set_cookieView, name='set_cookie'),
    path('set_session/', set_sessionView, name='set_session'),
    path('get_session/', get_sessionView, name='get_session'),

]
