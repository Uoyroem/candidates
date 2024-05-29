# Импорт стандартных библиотек Django для тестирования
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

# Импорт модели Document из текущего модуля
from .models import Document


class DocumentModelTest(TestCase):
    """
    Класс для тестирования модели Document.
    """
    def setUp(self):
        """
        Метод setUp выполняется перед каждым тестовым методом.
        Здесь мы создаем пользователя и документ для тестирования.
        """
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.document = Document.objects.create(title='Test Document', description='Test Description', user=self.user)

    def test_text_content(self):
        """
        Тест проверяет, что title документа соответствует ожидаемому.
        """
        expected_object_name = f'{self.document.title}'
        self.assertEquals(expected_object_name, 'Test Document')


class DocumentListViewTest(TestCase):
    """
    Класс для тестирования представления списка документов.
    """
    def setUp(self):
        """
        Метод setUp выполняется перед каждым тестовым методом.
        Здесь мы создаем пользователя, документ и клиент для тестирования.
        """
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.document = Document.objects.create(title='Test Document', description='Test Description', user=self.user)
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_view_url_exists_at_proper_location(self):
        """
        Тест проверяет, что URL представления существует и возвращает ожидаемый статус ответа.
        """
        resp = self.client.get('/documents/')
        self.assertEqual(resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        """
        Тест проверяет, что URL представления доступен по его имени и возвращает ожидаемый статус ответа.
        """
        resp = self.client.get(reverse('document_list'))
        self.assertEqual(resp.status_code, 302)
