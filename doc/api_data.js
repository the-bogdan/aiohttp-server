define({ "api": [
  {
    "type": "post",
    "url": "/orders",
    "title": "Crate new order",
    "name": "OrdersCreate",
    "group": "Orders",
    "description": "<p>Create new order</p>",
    "examples": [
      {
        "title": "json request body example",
        "content": "{\n  \"data\": {\n    \"attributes\": {\n      \"user_id\": 2\n    }\n  }\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 1,\n    \"model_type\": \"orders\",\n    \"attributes\": {\n      \"id\": \"1\",\n      \"user_id\": \"2\",\n      \"created_at\": \"2021-04-15 11:17:17\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:17:17\",\n      \"updated_by\": null,\n      \"deleted_at\": null,\n      \"deleted_by\": null\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/orders.py",
    "groupTitle": "Orders"
  },
  {
    "type": "delete",
    "url": "/orders/{id}",
    "title": "Delete order",
    "name": "OrdersDelete",
    "group": "Orders",
    "description": "<p>Delete order by id</p>",
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 1,\n    \"model_type\": \"orders\",\n    \"attributes\": {\n      \"id\": \"1\",\n      \"user_id\": \"1\",\n      \"created_at\": \"2021-04-15 11:17:17\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:20:01\",\n      \"updated_by\": \"2\",\n      \"deleted_at\": \"2021-04-15 11:21:41\",\n      \"deleted_by\": \"2\"\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/orders.py",
    "groupTitle": "Orders"
  },
  {
    "type": "get",
    "url": "/orders",
    "title": "Get orders array",
    "name": "OrdersGet",
    "group": "Orders",
    "description": "<p>Get all orders in array</p>",
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": [\n    {\n      \"id\": 3,\n      \"model_type\": \"orders\",\n      \"attributes\": {\n        \"id\": \"3\",\n        \"user_id\": \"1\",\n        \"created_at\": \"2021-04-15 11:22:24\",\n        \"created_by\": \"2\",\n        \"updated_at\": \"2021-04-15 11:22:24\",\n        \"updated_by\": null,\n        \"deleted_at\": null,\n        \"deleted_by\": null\n      }\n    }\n  ],\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/orders.py",
    "groupTitle": "Orders"
  },
  {
    "type": "get",
    "url": "/orders/{id}",
    "title": "Get order by id",
    "name": "OrdersGetByID",
    "group": "Orders",
    "description": "<p>Get order by id if exists else 400</p>",
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 3,\n    \"model_type\": \"orders\",\n    \"attributes\": {\n      \"id\": \"3\",\n      \"user_id\": \"1\",\n      \"created_at\": \"2021-04-15 11:22:24\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:22:24\",\n      \"updated_by\": null,\n      \"deleted_at\": null,\n      \"deleted_by\": null\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/orders.py",
    "groupTitle": "Orders"
  },
  {
    "type": "put",
    "url": "/orders/{id}",
    "title": "Update order",
    "name": "OrdersUpdate",
    "group": "Orders",
    "description": "<p>Update order by id</p>",
    "examples": [
      {
        "title": "json request body example",
        "content": "{\n  \"data\": {\n    \"attributes\": {\n      \"user_id\": 1\n    }\n  }\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 1,\n    \"model_type\": \"orders\",\n    \"attributes\": {\n      \"id\": \"1\",\n      \"user_id\": \"1\",\n      \"created_at\": \"2021-04-15 11:17:17\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:20:01\",\n      \"updated_by\": \"2\",\n      \"deleted_at\": null,\n      \"deleted_by\": null\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/orders.py",
    "groupTitle": "Orders"
  },
  {
    "type": "post",
    "url": "/users",
    "title": "Crate new user",
    "name": "UsersCreate",
    "group": "Users",
    "description": "<p>Create new users</p>",
    "examples": [
      {
        "title": "json request body example",
        "content": "{\n  \"data\": {\n    \"attributes\": {\n      \"first_name\": \"Bogdan\",\n      \"last_name\": \"Parshintsev\",\n      \"nickname\": \"asdf\",\n      \"password\": \"asdfasdf\"\n    }\n  }\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 4,\n    \"model_type\": \"users\",\n    \"attributes\": {\n      \"id\": \"4\",\n      \"first_name\": \"Bogdan\",\n      \"last_name\": \"Parshintsev\",\n      \"family_name\": null,\n      \"created_at\": \"2021-04-15 11:35:19\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:35:19\",\n      \"updated_by\": null,\n      \"deleted_at\": null,\n      \"deleted_by\": null\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/users.py",
    "groupTitle": "Users"
  },
  {
    "type": "delete",
    "url": "/users/{id}",
    "title": "Delete user",
    "name": "UsersDelete",
    "group": "Users",
    "description": "<p>Delete user by id</p>",
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 4,\n    \"model_type\": \"users\",\n    \"attributes\": {\n      \"id\": \"4\",\n      \"first_name\": \"Bogdann\",\n      \"last_name\": \"Parshintsev\",\n      \"family_name\": null,\n      \"created_at\": \"2021-04-15 11:35:19\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:38:49\",\n      \"updated_by\": \"2\",\n      \"deleted_at\": \"2021-04-15 11:40:02\",\n      \"deleted_by\": \"2\"\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/users.py",
    "groupTitle": "Users"
  },
  {
    "type": "get",
    "url": "/users",
    "title": "Get users array",
    "name": "UsersGet",
    "group": "Users",
    "description": "<p>Get all users in array</p>",
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": [\n    {\n      \"id\": 1,\n      \"model_type\": \"users\",\n      \"attributes\": {\n        \"id\": \"1\",\n        \"first_name\": \"Система\",\n        \"last_name\": \"System\",\n        \"family_name\": null,\n        \"created_at\": \"2021-04-15 06:42:08\",\n        \"created_by\": \"1\",\n        \"updated_at\": \"2021-04-15 06:42:08\",\n        \"updated_by\": \"1\",\n        \"deleted_at\": null,\n        \"deleted_by\": null\n      }\n    },\n    {\n      \"id\": 2,\n      \"model_type\": \"users\",\n      \"attributes\": {\n        \"id\": \"2\",\n        \"first_name\": \"admin\",\n        \"last_name\": \"admin\",\n        \"family_name\": null,\n        \"created_at\": \"2021-04-15 06:42:08\",\n        \"created_by\": \"1\",\n        \"updated_at\": \"2021-04-15 06:42:08\",\n        \"updated_by\": \"1\",\n        \"deleted_at\": null,\n        \"deleted_by\": null\n      }\n    }\n  ],\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/users.py",
    "groupTitle": "Users"
  },
  {
    "type": "get",
    "url": "/users/{id}",
    "title": "Get user by id",
    "name": "UsersGetByID",
    "group": "Users",
    "description": "<p>Get user by id if exists else 400</p>",
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 2,\n    \"model_type\": \"users\",\n    \"attributes\": {\n      \"id\": \"2\",\n      \"first_name\": \"admin\",\n      \"last_name\": \"admin\",\n      \"family_name\": null,\n      \"created_at\": \"2021-04-15 06:42:08\",\n      \"created_by\": \"1\",\n      \"updated_at\": \"2021-04-15 06:42:08\",\n      \"updated_by\": \"1\",\n      \"deleted_at\": null,\n      \"deleted_by\": null\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/users.py",
    "groupTitle": "Users"
  },
  {
    "type": "put",
    "url": "/users/{id}",
    "title": "Update users",
    "name": "UsersUpdate",
    "group": "Users",
    "description": "<p>Update user by id</p>",
    "examples": [
      {
        "title": "json request body example",
        "content": "{\n  \"data\": {\n    \"attributes\": {\n      \"first_name\": \"Bogdann\"\n    }\n  }\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "response body example",
          "content": "{\n  \"data\": {\n    \"id\": 4,\n    \"model_type\": \"users\",\n    \"attributes\": {\n      \"id\": \"4\",\n      \"first_name\": \"Bogdann\",\n      \"last_name\": \"Parshintsev\",\n      \"family_name\": null,\n      \"created_at\": \"2021-04-15 11:35:19\",\n      \"created_by\": \"2\",\n      \"updated_at\": \"2021-04-15 11:38:49\",\n      \"updated_by\": \"2\",\n      \"deleted_at\": null,\n      \"deleted_by\": null\n    }\n  },\n  \"included\": {}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "app/controllers/users.py",
    "groupTitle": "Users"
  }
] });
