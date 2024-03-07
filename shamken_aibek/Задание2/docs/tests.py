from django.test import TestCase
from docs.utils import add_two_num


# Не знаю что добавить, но создаются так
class Task2TestCase(TestCase):
    def test_add_two_num(self):
        result = add_two_num(2, 3)
        self.assertEqual(result, 5)
