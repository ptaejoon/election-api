"""
ORM for Promise table
"""
from app.models.base import BaseORM
from sqlalchemy.sql.base import Column
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String
from datetime import datetime

class PromiseORM(BaseORM):
    __tablename__ = "promise"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Promise {self.title}>"

    def __str__(self):
        return f"<Promise {self.title}>"

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash(self.title)


class PromiseFriendlinessORM(BaseORM):
    __tablename__ = "promise_friendliness"
    id = Column(Integer, primary_key=True)
    promise_id = Column(Integer)
    # 테이블 구성 고민 필요
    friendliness_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f"<PromiseFriendliness {self.promise_id}>"

    def __str__(self):
        return f"<PromiseFriendliness {self.promise_id}>"

    def __eq__(self, other):
        return self.promise_id == other.promise_id

    def __hash__(self):
        return hash(self.promise_id)