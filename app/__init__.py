from app.lib.database import configure_sqlalchemy

_db_uri = "mysql+pymysql://roly:rolypoly@localhost:3306/election"
# connect db to real server / setting value through github secret (or another private way)
configure_sqlalchemy(
    connection_uri=_db_uri,
    engine_options={
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 3600,
    },
)