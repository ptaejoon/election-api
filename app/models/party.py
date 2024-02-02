"""
ORM for party table
"""
from .base import BaseORM
from sqlalchemy import Column, Integer, String


class PartyORM(BaseORM):
    __tablename__ = "party"
    name = Column(String(100), Primary_key=True)
    image = Column(String(300))

    def __repr__(self):
        return f"<Party {self.name}>"

    def __str__(self):
        return f"<Party {self.name}>"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
