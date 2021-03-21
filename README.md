# Рест сервер на iohttp с использованием SQLAlchemy 1.4

Python 3.8


## Запуск

Склонировать себе командой git clone

Далее создать виртуальное окружение и установить зависимости:


```
virtualenv .env -p python3.8
source .env/bin/activate
pip install -r requirements.txt
```

Переименовать файл config_example.py в config.py и указать внутри все необходимые credentials для подключения к postgres

```
cp config_example.py config.py
```

Для создания всех таблиц запустить manage.py  с флагом -m (--migrate) !!!Внимание перед созданием таблиц все старые будут удалены и данные утеряны. Лучше создать отдельную тестовую базу в postgres для тестирования!!!:


```
python manage.py -m 
```

Для запуска сервиса запустить manage.py с флагом -r (--run):

```
python manage.py -r
```

## Доступ к api:

Для всех api необходимо делать запросы с basic auth. По умолчанию создан пользователь с логином и паролем admin:admin

### User

#### GET /users/{id}
Получения данных пользователя через id

Пример ответа сервиса: 

```json
{
  "data": {
    "id": 1,
    "model_type": "users",
    "attributes": {
      "family_name": null,
      "first_name": "админ",
      "id": 1,
      "last_name": "admin"
    }
  },
  "included": {}
}
```

#### POST /users
Получение пользователей с применением фильтров по атрибутам, также возможно получить сущности orders и products через запрос с with_entities. 

Пример запроса:

```json
{
  "filters": [
    {
      "type": "id",
      "value": 1
    }
  ],
  "with_entities": [
    "orders",
    "products"
  ]
}
```

Пример ответа сервера:

```json
{
  "data": [
    {
      "id": 1,
      "model_type": "users",
      "attributes": {
        "family_name": null,
        "first_name": "админ",
        "id": 1,
        "last_name": "admin"
      }
    }
  ],
  "included": {
    "orders": [
      {
        "id": 1,
        "model_type": "orders",
        "attributes": {
          "id": 1,
          "user_id": 1,
          "number": 12
        }
      },
      {
        "id": 2,
        "model_type": "orders",
        "attributes": {
          "id": 2,
          "user_id": 1,
          "number": 12
        }
      }
    ],
    "products": [
      {
        "id": 1,
        "model_type": "products",
        "attributes": {
          "price": 12,
          "name": "asdf",
          "left_in_stock": 12,
          "id": 1,
          "description": "asdf"
        }
      },
      {
        "id": 2,
        "model_type": "products",
        "attributes": {
          "price": 12,
          "name": "asdfasdf",
          "left_in_stock": 21,
          "id": 2,
          "description": "asdfasdfa"
        }
      }
    ]
  }
}
```

#### PUT /users 
Создание пользователя

Пример запроса:
```json
{
  "data": {
    "id": null,
    "model_type": "users",
    "attributes": {
      "id": null,
      "first_name": "asdf",
      "family_name": null,
      "last_name": "asdf",
      "_nickname": "asdf",
      "_password": "asdf"
    }
  }
}
```

Ответ сервера:

```json
{
  "data": {
    "id": 4,
    "model_type": "users",
    "attributes": {
      "first_name": "asdf",
      "family_name": null,
      "last_name": "asdf",
      "id": 4
    }
  },
  "included": {}
}
```

#### PATCH /users/{id}
Редактирование пользователя


Пример запроса
```json
{
  "data": {
    "attributes": {
      "id": 4,
      "first_name": "asdf",
      "family_name": null,
      "last_name": "asdfasdfasdf",
      "_nickname": "asdf",
      "_password": "asdf"
    }
  }
}
```

Ответ сервера
```json
{
  "data": {
    "id": 4,
    "model_type": "users",
    "attributes": {
      "id": 4,
      "first_name": "asdf",
      "family_name": null,
      "last_name": "asdfasdfasdf"
    }
  },
  "included": {}
}
```

#### DELETE /users/{id}
Удаление пользователя

Ответ сервера в случае успешного удаления:
```join
{
  "data": {
    "id": 4,
    "model_type": "users",
    "attributes": {
      "id": 4,
      "first_name": "asdf",
      "family_name": null,
      "last_name": "asdfasdfasdf"
    }
  },
  "included": {}
}
```

#### PUT /users/follow/{id}
Подписаться на пользователя

Ответ сервара в случае успешной подписки:
```json
{
  "data": {
    "id": 1,
    "model_type": "users_relations",
    "attributes": {
      "dst_user_id": 2,
      "src_user_id": 1,
      "id": 1
    }
  },
  "included": {}
}
```

#### GET /users/followers
Получить всех подписанных пользователей

Пример ответа сервера:

```json
{
  "data": [
    {
      "id": 2,
      "model_type": "users",
      "attributes": {
        "first_name": "asdf",
        "id": 2,
        "family_name": "asdf",
        "last_name": "asdf"
      }
    }
  ],
  "included": {}
}
```

### Order

#### GET /orders/{id}
Получения данных о заказе через id

Пример ответа сервиса: 

```json
{
  "data": {
    "id": 1,
    "model_type": "orders",
    "attributes": {
      "number": 150,
      "user_id": 1,
      "id": 1
    }
  },
  "included": {}
}
```
#### POST /orders
Получение заказов с применением фильтров по атрибутам, также возможно получить сущности users и products через запрос с with_entities. 

Пример запроса:

```json
{
  "filters": [
    {
      "type": "id",
      "value": 1
    }
  ],
  "with_entities": [
    "users",
    "products"
  ]
}
```

Пример ответа сервера:

```json
{
  "data": [
    {
      "id": 1,
      "model_type": "orders",
      "attributes": {
        "id": 1,
        "user_id": 1,
        "number": 150
      }
    }
  ],
  "included": {
    "users": [
      {
        "id": 1,
        "model_type": "users",
        "attributes": {
          "family_name": null,
          "first_name": "админ",
          "id": 1,
          "last_name": "admin"
        }
      }
    ],
    "products": [
      {
        "id": 1,
        "model_type": "products",
        "attributes": {
          "name": "asdf",
          "price": 123,
          "left_in_stock": 123,
          "id": 1,
          "description": "asdf"
        }
      }
    ]
  }
}
```

#### PUT /orders
Создание заказа, аналогично PUT /users

#### PATCH /orders/{id}
Внесение изменений в сущность заказа, аналогично PATCH /users/{id}

#### DELETE /orders/{id}
Удаление заказа, аналогично DELETE /users/{id}
