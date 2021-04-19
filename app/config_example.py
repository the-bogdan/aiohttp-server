config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8000
    },
    "logs": {
        "logs_level": "INFO",
        "logs_path": "logs/aiohttp_server.log"
    },
    "postgres": {
        "username": "postgres",
        "password": "123456",
        "drivername": "postgresql+asyncpg",
        "database": "postgres",
        "host": "aiohttp_server_postgres13",
        "port": 5432
    }
}
