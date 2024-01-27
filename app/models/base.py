from sqlalchemy.orm import as_declarative, Query, Session
from typing import Type, TypeVar, Optional

from app.lib.database import with_session

C = TypeVar("C", bound="BaseORM")


@as_declarative()
class BaseORM:
    """
    Base class for all models.
    Define all db basic actions
    """
    _query = None
    def __init__(self: C, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create_query(cls: Type[C], *filter, session: Optional[Session] = None , **filter_by) -> Query:
        query = cls._query or session.query(cls)
        if filter:
            query = query.filter(*filter)
        if filter_by:
            query = query.filter_by(**filter_by)
        return query
    @classmethod
    @with_session
    def get(cls: Type[C], *filter, session: Optional[Session] = None, **filter_by) -> Optional[C]:
        query = cls.create_query(session=session,*filter,  **filter_by)
        return query.first()

    @classmethod
    @with_session
    def create(cls: Type[C],
               commit: bool = True,
               flush: bool = False,
               session: Optional[Session] = None,
               **kwargs
               ) -> C:
        return cls(**kwargs).save(commit=commit, flush=flush, session=session)
    # List, Create, Delete, Update 등의 기능을 추가할 수 있음

    @with_session
    def save(self,
             commit: bool = True,
             flush: bool = False,
             refresh: bool = True,
             merge: bool = False,
             session: Optional[Session] = None,
             ) -> C:
        """Save this object on database."""
        if merge:
            session.merge(self)
        else:
            session.add(self)
        if commit:
            session.commit()
        if flush:
            session.flush()
        if (commit or flush) and refresh:
            session.refresh(self)
        return self

    # [TODO] Delete, join, list