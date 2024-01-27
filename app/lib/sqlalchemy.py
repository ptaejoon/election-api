from app.lib.serializer import json_dumps
from app.lib.database import configure_sqlalchemy
from fastapi import FastAPI

engine_option = {
    "echo": False,
    "json_serializer": lambda data: json_dumps(data, indent=None),
    "pool_size": 10,
    "max_overflow": 20,
    "pool_recycle": 3600,
    "connect_args": {
        "charset": "utf8mb4",
    },
}


def set_sqlalchemy(app: FastAPI):
    configure_sqlalchemy(
        "uri",
        engine_options=engine_option,
    )
