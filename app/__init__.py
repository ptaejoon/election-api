from app.lib.database import configure_sqlalchemy
from os import environ
_db_uri = f"mysql+pymysql://{environ['DB_USER']}:{environ['DB_PWD']}@{environ['DB_HOST']}:3306/election"

configure_sqlalchemy(
    connection_uri=_db_uri,
    engine_options={
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 3600,
    },
)