# Настройка админки

## 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

## 2. Запуск нового проекта Django

```bash
python manage.py runserver
```

## 3. Применение миграций

```bash
python manage.py migrate
```

## 4. Создание суперпользователя

```bash
python manage.py createsuperuser
```

Следуйте инструкциям для создания учетных данных администратора.

## 5. Запуск сервера разработки

```bash
python manage.py runserver
```

Перейдите по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), чтобы получить доступ к административной панели.