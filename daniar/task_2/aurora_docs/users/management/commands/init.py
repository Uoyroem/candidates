from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    """
    Command - это класс команды управления Django.

    Он используется для создания начальных данных, включая суперпользователя и обычного пользователя.
    """

    # Описание команды
    help = 'Создание начальных данных'

    def handle(self, *args, **options):
        """
        Обработка команды.

        Если суперпользователь 'admin' не существует, он создается.
        Если обычный пользователь 'user' не существует, он также создается.
        """
        # Проверка наличия суперпользователя 'admin'
        if not User.objects.filter(username='admin').exists():
            # Создание суперпользователя 'admin'
            User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Успешно создан новый суперпользователь'))

        # Проверка наличия обычного пользователя 'user'
        if not User.objects.filter(username='user').exists():
            # Создание обычного пользователя 'user'
            User.objects.create_user('user', 'user@gmail.com', 'user')
            self.stdout.write(self.style.SUCCESS('Успешно создан новый пользователь'))
