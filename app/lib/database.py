from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker
from app.lib.serializer import json_dumps
from functools import wraps
from contextlib import contextmanager

__all__ = [
    "with_session"
]

engine: Optional[Engine] = None
SessionMaker: Optional[scoped_session] = None


def configure_sqlalchemy(
        connection_uri: str,
        engine_options: Optional[dict] = None,
):
    """Configure SQLAlchemy engine and scoped session."""
    global engine, SessionMaker

    if engine:
        return

    options = {
        "echo": False,
        "json_serializer": lambda data: json_dumps(data, indent=None),
    }
    if engine_options:
        options.update(engine_options)
    engine = create_engine(connection_uri, **engine_options or {})
    SessionMaker = scoped_session(sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    ),
    )


def get_engine() -> Engine:
    """Return SQLAlchemy engine."""
    global engine
    if not engine:
        raise Exception("SQLAlchemy engine is not configured.")
    return engine


def get_session_maker() -> scoped_session:
    """Return SQLAlchemy session maker."""
    global SessionMaker
    if not SessionMaker:
        raise Exception("SQLAlchemy session maker is not configured.")
    return SessionMaker


@contextmanager
def session_scope():
    """
    Provide a transactional scope around a series of operations.
    with session_scope() as session:
        session.query(...)
    """
    global SessionMaker
    session = SessionMaker()
    try:
        yield session
        session.commit()
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


def with_session(func):
    """
    함수에 session 인자가 있으면 그대로 실행하고,
    없으면 session_scope()로 session을 생성해서 실행한다.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "session" in kwargs:
            return func(*args, **kwargs)
        with session_scope() as session:
            return func(*args, session=session, **kwargs)

    return wrapper
