from sqlalchemy import Column, desc
from sqlalchemy.orm import as_declarative, Query, Session
from typing import Type, TypeVar, Optional, List, Union, Literal

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
    def create_query(
            cls: Type[C],
            *filters,
            order_by: Optional[Union[Column, List[Column], desc]] = None,
            limit: int = None,
            offset: int = None,
            session: Optional[Session] = None,
            clear: bool = True,
            **filter_by,
    ) -> Query:
        query = cls._query or session.query(cls)
        if filters:
            query = query.filter(*filters)
        if filter_by:
            query = query.filter_by(**filter_by)
        if order_by is not None:
            if isinstance(order_by, list):
                query = query.order_by(*order_by)
            else:
                query = query.order_by(order_by)
        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)
        if clear:
            cls._query = None
        return query

    @classmethod
    @with_session
    def get(cls: Type[C], *filters, session: Optional[Session] = None, **filter_by) -> Optional[C]:
        query = cls.create_query(*filters, session=session, **filter_by)
        return query.first()

    @classmethod
    @with_session
    def list(cls: Type[C],
             *filters,
             order_by: Optional[Union[Column, List[Column], desc]] = None,
             limit: int = None,
             offset: int = None,
             session: Optional[Session] = None,
             **filter_by
             ) -> List[C]:
        query = cls.create_query(
            *filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            session=session,
            **filter_by
        )
        return query.all()

    @classmethod
    @with_session
    def create(cls: Type[C],
               commit: bool = True,
               flush: bool = False,
               session: Optional[Session] = None,
               **kwargs
               ) -> C:
        return cls(**kwargs).save(commit=commit, flush=flush, session=session)

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

    @with_session
    def delete(self,
               commit: bool = True,
               flush: bool = False,
               session: Optional[Session] = None,
               ) -> C:
        session.delete(self)
        if commit:
            session.commit()
        if flush:
            session.flush()
        return self

    @classmethod
    @with_session
    def delete_all(cls: Type[C],
                   *filters,
                   synchronize_session: Literal[False, "evaluate", "fetch"] = "evaluate",
                   commit: bool = True,
                   flush: bool = False,
                   session: Optional[Session] = None,
                   **filter_by,
                   ) -> int:
        query = cls.create_query(*filters, session=session, **filter_by)
        count = query.delete(synchronize_session=synchronize_session)
        if commit:
            session.commit()
        if flush:
            session.flush()
        return count

    @classmethod
    @with_session
    def join(cls: Type[C],
             *cols,
             join_type: Literal["inner", "outer"] = "inner",
             session: Session = None,
             ) -> Type[C]:
        query = cls.create_query(session=session, clear=False)
        if join_type == "inner":
            query = query.join(*cols)
        elif join_type == "outer":
            query = query.outerjoin(*cols)
        cls._query = query
        return cls
