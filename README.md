# Django-приложение для реализации древовидного меню

Это Django-приложение реализует древовидное меню с учетом следующих требований:

1. Реализовано через Template Tag
2. Все элементы над выбранным пунктом развернуты, а первый уровень вложенности под выбранным пунктом также развернут.
3. Меню хранится в БД.
4. Меню редактируется в стандартной админке Django.
5. Активный пункт меню определяется на основе URL текущей страницы.
6. Несколько меню на одной странице определяются по названию.
7. При клике на меню происходит переход по заданному URL (явно или через named url).
8. Отрисовка меню требует ровно 1 запрос к БД для каждого меню.

## Инструкции по установке и использованию

1. Клонируйте репозиторий:

```
git clone https://github.com/your_username/django-menu.git
```

2. Создайте и активируйте virtualenv:

```
python -m venv env
source env/bin/activate
```

3. Установите зависимости:

```
pip install -r requirements.txt 
```

4. Перейдите в каталог проекта:

```
cd test-project
```

5. Примените миграции:

```
python manage.py migrate
```

6. Создайте суперпользователя:

```
python manage.py createsuperuser
```

7. Запустите сервер:

```
python manage.py runserver
```
