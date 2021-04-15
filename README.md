# Рест сервер на iohttp с использованием SQLAlchemy 1.4

**Python 3.9**

[**Документация по api**](https://bparshintsev.github.io/aiohttp-server/)

## Запуск сервиса

Склонировать себе командой git clone

Далее создать виртуальное окружение и установить зависимости:


```shell
virtualenv .env -p python3.9
source .env/bin/activate
pip install -r requirements.txt
```

Переименовать файл config_example.py в config.py и указать внутри все необходимые credentials для подключения к postgres

```shell
cp config_example.py config.py
```

Для создания всех таблиц запустить manage.py  с флагом -m (--migrate) !!!Внимание перед созданием таблиц все старые будут удалены и данные утеряны. Лучше создать отдельную тестовую базу в postgres для тестирования!!!:


```shell
python manage.py -m 
```

Для запуска сервиса запустить manage.py с флагом -r (--run):

```shell
python manage.py -r
```

## Сборка документации
Для сборки документации использутеся apidoc, предварительно его необходимо поствать через npm
```shell
npm install -g apidoc
```
Для сборки документации выполнить:
```shell
apidoc -i ./app/ -o docs
```

## Доступ к api:

Для всех api необходимо делать запросы с basic auth. 
По умолчанию создан пользователь с логином и паролем
```shell
admin:admin
```

## Работа с CRUD
В проекте представлен базовый функционал для выполнения всех CRUD операций для всех таблиц базы данных.
Для этого достаточно выполнить один из базывых апи по url, который зависит от названия таблицы.

Для получения сущности из любой таблицы по id:
```
GET /{database_model}/{id}
```

Для получения сущности из любой таблицы:
```
GET /{database_model}
```

Для создания сущности в любой таблице:
```
POST /{database_model}
```

Для изменения сущности в любой таблице:
```
PUT /{database_model}/{id}
```

Для удаления сущности из любой таблицы:
```
DELETE /{database_model}/{id}
```

Для каждого из представленных методов присутствует валидация по всем полям.

Структура запросов для создания и измениния сущности:
```json
{
  "data": {
    "attributes": {}
  }
}
```
где в attributes хранятся поля которые необходимо внести в базу данных в таблицу

## Создание новой таблицы
Для создания новой таблицы достаточно создать SQLAlchemy ORM модель этой таблице в файле
database/model.py и всё! Больше ничего делать не нужно, для модели будут сразу поддерживаться
полный CRUD функционал с валидацией по полям на создании и измении в том числе

## Системные поля
Все модели БД необходимо наследовать от MixinCRUD, который добавляет 6 системных полей, которые, в свою очередь, 
позволяют определять кто и когда создал / изменил / удалил сущность в базе данных. В проекте используется так называемое
"мягкое удаление", т.е. из базы данных физически записи не удаляются, а просто помечаются как удаленные, для этого
также есть системные поля, добавляемые MixinCRUD. Системные поля нельзя изменить через вызов API, даже если вы
передадите из в аттрибутах.

Вот список системных полей:
```json
[
  "created_at",
  "created_by",
  "updated_at",
  "updated_by",
  "deleted_at",
  "deleted_by"
]
```

## Модели:

В документации к API, указанной выше, представлена документация только для User и Order, 
но точно таким же путем можно взаимодействовать со всеми нижеперечисленными 
таблицами

### User
```json
{
  "table_name": "users",
  "attributes": {
    "id": {"type":  "number", "required":  false},
    "first_name": {"type":  "string", "required":  true},
    "last_name": {"type":  "string", "required":  true},
    "family_name": {"type":  "string", "required":  false},
    "nickname": {"type":  "string", "required":  true},
    "password": {"type":  "string", "required":  true}
  }
}
```
### Order
```json
{
  "table_name": "orders",
  "attributes": {
    "id": {"type":  "number", "required":  false},
    "user_id": {"type":  "number", "required":  true}
  }
}
```

### Product
```json
{
  "table_name": "products",
  "attributes": {
    "id": {"type":  "number", "required":  false},
    "name": {"type":  "string", "required":  true},
    "description": {"type":  "string", "required":  false},
    "price": {"type":  "float", "required":  true}
  }
}
```

### OrderProduct
```json
{
  "table_name": "orders_products",
  "attributes": {
    "id": {"type":  "number", "required":  false},
    "order_id": {"type":  "number", "required":  true},
    "product_id": {"type":  "number", "required":  true}
  }
}
```
