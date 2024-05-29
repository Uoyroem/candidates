# README.md

# Aurora Docs

Aurora Docs - это веб-приложение для управления документами, написанное на Python с использованием Django. Проект выполнен в рамках тестового задания для компании Aurora Данияром Исмаиловым (github.com/zsz13).

## Особенности

- Создание, редактирование и удаление документов (CRUD).
- Просмотр списка всех документов.
- Аутентификация и авторизация пользователей. Пользователи могут войти в систему, а затем создавать, редактировать и удалять документы. Пользователи имеют разные уровни доступа в зависимости от их роли.
- Возможность выбора между двумя базами данных: SQLite и PostgreSQL.
- Два предустановленных пользователя: администратор (admin@gmail.com, пароль: admin) и обычный пользователь (user@gmail.com, пароль: user).
- Тесты для проверки функциональности приложения.

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/zsz13/aurora_docs.git
```

2. Перейдите в каталог проекта:

```bash
cd aurora_docs
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Примените миграции:

```bash
python manage.py migrate
```

5. Запустите сервер разработки:

```bash
python manage.py runserver
```

Теперь вы можете открыть веб-браузер и перейти по адресу `http://localhost:8000` для доступа к приложению.

## Запуск с использованием Docker

1. Соберите образ Docker:

```bash
docker-compose build
```

2. Запустите контейнеры Docker:

```bash
docker-compose up
```

Теперь вы можете открыть веб-браузер и перейти по адресу `http://localhost:8000` для доступа к приложению.

## English

# Aurora Docs

Aurora Docs is a document management web application written in Python using Django. The project was completed as a test assignment for Aurora company by Daniyar Ismailov (github.com/zsz13).

## Features

- Create, edit, and delete documents (CRUD).
- View a list of all documents.
- User authentication and authorization. Users can log in and then create, edit, and delete documents. Users have different access levels depending on their role.
- Ability to choose between two databases: SQLite and PostgreSQL.
- Two pre-set users: an administrator (admin@gmail.com, password: admin) and a regular user (user@gmail.com, password: user).
- Tests for checking the functionality of the application.

## Installation and Running

1. Clone the repository:

```bash
git clone https://github.com/zsz13/aurora_docs.git
```

2. Navigate to the project directory:

```bash
cd aurora_docs
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

Now you can open your web browser and navigate to `http://localhost:8000` to access the application.

## Running with Docker

1. Build the Docker image:

```bash
docker-compose build
```

2. Start the Docker containers:

```bash
docker-compose up
```

Now you can open your web browser and navigate to `http://localhost:8000` to access the application.