"""
ORM for district table
"""
from sqlalchemy import Column, String

from app.models import BaseORM


class DistrictORM(BaseORM):
    __tablename__ = "district"
    parent_district = Column(String(20), nullable=True, primary_key=True)
    name = Column(String(50), nullable=False, primary_key=True)

    def __repr__(self):
        return f"<District {self.name}, {self.parent_district}>"

    def __str__(self):
        return f"<District {self.name}, {self.parent_district}>"