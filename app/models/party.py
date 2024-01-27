"""
ORM for party table
"""
from base import BaseORM

class PartyORM(BaseORM):
    __tablename__ = "party"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Party {self.name}>"

    def __str__(self):
        return f"<Party {self.name}>"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)