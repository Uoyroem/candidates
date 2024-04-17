\* - это особо не важные пункты.\
\! - не следовал по требованию ТЗ.

Сохранять миграций это нормально если оно только одно.
Некоторые недостатки могут быть из за моего неопытности.

# Ерасыл 2.3/5
## ТЗ
- Создать конвертер docx, xlsx в pdf,
- Создать наподобий файлового менеджера в Django, авторизация и аутентификация должна быть через `email`.

## Плюсы
- Использовал `logging`, 
- Работает конвертер docx в pdf,
- Использует функцию `main` с проверкой `__name__ == "__main__"`*.
## Минусы
- Не работает конвертер xlsx в pdf!,
- Не использовал аннотаций*,
- Нету `requirements.txt`!,
- Отправил код с базой данных и с миграциями*.
- Авторизация и аутентификация не через `email` а через `username`!,
- Не использовал `Git`*,
- Не использовал хотя-бы `bootstrap` для стилей*,
- Стили не очень, их даже нет,
- Файл загуржается, но их список нигде не показывает!,
- Короче мне больно на это смотреть.


# Нургали 4.5/5
## ТЗ 
Пусть создаст app и в нем такие модели: 
1. Документ основания.
2. Контрагент.
3. Ответственный (Отдельная моделька у которого есть ID и имя на пример  20277 - Иващенко Андрей где  20277 это ID а "Иващенко Андрей" first_name и last_name)


Каждая строка в этом файле это 1 Документ основания. 
В нем есть информация о Контрагенте ФИО пользователей. 

БИН контрагентов не должны повторяться.
Так же и ID ответственных


Надо написать форму который принимает JSON файл. 
При возникновении ошибки надо его показывать на странице. 
Надо учитывать что некоторые поля могут быть не заполнены и написать для таких случай исключение

После импорта надо кидать на страницу в котором есть таблица. таблица должна состоять из всех полней что есть у модели включая поля привязанных моделей (Контрагент, Ответственный)

## Плюсы
- Показывать ошибку при импорте если есть ошибка,
- Использовал `bootstrap`*,
- Импорт работает!,
- Хорошо использует Django ORM,
- БИН Контрагентов и ID Ответсвенных не повторяются, потому что поле `Counteragent.bin` использует `unique=True`,
- Для пустых полей написаны исключение,
- Поле импорта показывает таблицу.
- Поиск работает.
## Минусы
- Не использовал аннотаций*,
- Нету `requiremenets.txt`,
- Не использовал `Git`*,
- Не использовал классы в `views.py`*,
- Отправил код с базой данных и с миграциями*,
- Не перенёс логику импорт в отдельный файл, а сразу написал в `views.py`*,
- Таблица слишком большой и выходит за границы экрана*.
- При повторном импорте Документ основания повторяются.

# Шамкен Айбек 4.6/5
## ТЗ
- Создать конвертер docx, xlsx в pdf,
- Создать наподобий файлового менеджера в Django, авторизация и аутентификация должна быть через `email`.
## ???
- Конверт docx в pdf вроде должно работать, надо проверить в ПК где есть Microsoft Word!.
## Плюсы
- Есть `requirements.txt` в Задание2!,
- Использовал `logging`, 
- Использует функцию `main_window` с проверкой `__name__ == "__main__"`*,
- Использовал `bootstrap`*,
- Стили очень приятные для глаз,
- Использует `app_name` в `urls.py`,
- Использует классы,
- Использует `permissions`,
- Использует `managment.commands`,
- В целом круто пишет код.
## Минусы
- Не использовал `Git`*,
- Нету преоброзование xlsx в pdf!,
- Не использовал аннотаций*,
- Если немного подправить стили будет вообще класс*.
- Немного не следует `PEP8`, имена классов `docs_indexView` должный писаться по крайней мере `DocsIndexView`,
- Авторизация и аутентификация не через `email` а через `username`!,
- Отправил код с базой данных и с миграциями*.

# Жасулан 3.7/5
## ТЗ
Пусть создаст app и в нем такие модели: 
1. Документ основания.
2. Контрагент.
3. Ответственный (Отдельная моделька у которого есть ID и имя на пример  20277 - Иващенко Андрей где  20277 это ID а "Иващенко Андрей" first_name и last_name)


Каждая строка в этом файле это 1 Документ основания. 
В нем есть информация о Контрагенте ФИО пользователей. 

БИН контрагентов не должны повторяться.
Так же и ID ответственных


Надо написать форму который принимает JSON файл. 
При возникновении ошибки надо его показывать на странице. 
Надо учитывать что некоторые поля могут быть не заполнены и написать для таких случай исключение

После импорта надо кидать на страницу в котором есть таблица. таблица должна состоять из всех полней что есть у модели включая поля привязанных моделей (Контрагент, Ответственный)

## Плюсы
- Использовал `Git`*,
- Импорт работает!,
- БИН Контрагентов и ID Ответсвенных не повторяются,
- Поле импорта показывает таблицу,
- Поиск работает.
## Минусы
- Нету `requiremenets.txt`,
- Не использовал классы в `views.py`*,
- При открытий главной `/` страницы, показывает 404, а не перекидовает на работающию*,
- Не использовал хотя-бы `bootstrap` для стилей*,
- Стили не очень, их даже нет*,
- При повторном импорте Документ основания повторяются.

# Miku 4.7/5
## ТЗ
- Создать конвертер docx, xlsx в pdf,
- Создать наподобий файлового менеджера в Django, авторизация и аутентификация должна быть через `email`.

## ???
- Конверт docx в pdf вроде должно работать, надо проверить в ПК где есть Microsoft Word!.

## Плюсы
- Использует функцию `main` с проверкой `__name__ == "__main__"`*,
- Пишет комментарий для кода!,
- Есть `requirements.txt`!,
- Использовал `logging`!,
- Работает конвертер с xlsx в pdf!,
- Есть `.gitignore`,
- Разделил frontend и backend, что очень хорошо!,
- Использует Django Rest Framework,
- Авторизация и аутентификация через `email`,
- CRUD документов работает,
- Полное обновление работает, а частичное нет, хотя запрос кидается как `PATCH`, но работает как `PUT`,
- Использует JWT токены,
- Умеет писать на JavaScript, если бы использовал `async/await`, то было бы вообще круто.
## Минусы
- Добавил папку migrations в `.gitignore`, без него не работает миграций в Django, надо хотя бы оставить папку migrations и файл \_\_init__.py, а остальное можно игнорить.

# Adilhan 3.9/5
## ТЗ
- Создать конвертер docx, xlsx в pdf,
- Создать наподобий файлового менеджера в Django, авторизация и аутентификация должна быть через `email`.
## ???
- Конверт docx в pdf вроде должно работать, надо проверить в ПК где есть Microsoft Word!.
## Плюсы
- Использует \_\_name__ == "\_\_main__",
- Работает конвертер xlsx в pdf, сделал довольно интересным образом, используя pandas и matplotlib,
- Авторизация и аутентификация работает хотя через `username`,
- Внешний вид страницы авторизация и аутентификация сайта очень хорошо сделан,
- CRUD документов работает. 
## Минусы
- Нету `requiremenets.txt`,
- Отправил медиа-файлы, базу данных и миграций,
- Авторизация и аутентификация не через `email` а через `username`!,


# Dude 3.8/5
## ТЗ
- Создать конвертер docx, xlsx в pdf,
- Создать наподобий файлового менеджера в Django, авторизация и аутентификация должна быть через `email`.
## ???
- Конверт docx в pdf вроде должно работать, надо проверить в ПК где есть Microsoft Word!.
## Плюсы
- Использует функцию `main` с проверкой `__name__ == "__main__"`*,
- Использовал `logging`!,
- Работает конвертер с xlsx в pdf!,
- Использует сигналы чтобы удалять файлы.
## Минусы
- Есть `requirements.txt`, но имеет неверный формат, короче не работает,
- Авторизация и аутентификация не работает,
- Внешний вид не очень.