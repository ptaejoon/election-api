"""
ORM for Promise table
"""
from app.models.base import BaseORM
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String


class PromiseORM(BaseORM):
    __tablename__ = "promise"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(500))

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

    def __repr__(self):
        return f"<PromiseFriendliness {self.promise_id}>"

    def __str__(self):
        return f"<PromiseFriendliness {self.promise_id}>"

    def __eq__(self, other):
        return self.promise_id == other.promise_id

    def __hash__(self):
        return hash(self.promise_id)
