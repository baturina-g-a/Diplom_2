## Дипломный проект. Задание 2: API

### Автотесты для проверки API сервиса Stellar Burgers

### Реализованные сценарии

Созданы автотесты, проверяющие эндпоинты:
1. Создание пользователя
2. Логин пользователя
3. Изменение данных пользователя
4. Создание заказа
5. Получение заказов конкретного пользователя

### Структура проекта

Папки:
- `methods` - пакет, содержащий файлы со вспомогательными классами по методам, файлы разделены по namespace;
- `tests` - пакет, содержащий папки, разделенные по namespace, с файлами, в каждом файле тесты по определенному методу;
- `allure_results` - allure-отчёты по прогону тестов.

Файлы: 
1. confest.py - файл с фикстурами;
2. data.py - файл с наборами тестовых данных;
3. helpers.py - файл со вспомогательными методами (в данном случае, на генерацию нового уникального пользователя);
4. requirements.txt - файл с внешними зависимостями.


### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание Allure-отчета**

>  `$ pytest tests --alluredir=allure_results`