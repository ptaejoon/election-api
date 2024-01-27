"""
ORM for party table
"""
from .base import BaseORM
from sqlalchemy import Column, Integer, String


class PartyORM(BaseORM):
    __tablename__ = "party"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    image = Column(String(300))

    def __repr__(self):
        return f"<Party {self.name}>"

    def __str__(self):
        return f"<Party {self.name}>"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
