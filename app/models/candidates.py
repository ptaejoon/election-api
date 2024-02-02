"""
ORM for candidates table
"""
from app.models.base import BaseORM
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String


class CandidatesPromiseRelationORM(BaseORM):
    __tablename__ = "candidates_promise_relation"
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer)
    promise_id = Column(Integer)

    def __repr__(self):
        return f"<CandidatePromiseRelation {self.candidate_id}>"

    def __str__(self):
        return f"<CandidatePromiseRelation {self.candidate_id}>"

    def __eq__(self, other):
        return self.candidate_id == other.candidate_id

    def __hash__(self):
        return hash(self.candidate_id)


class CandidatesORM(BaseORM):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    chinese_name = Column(String(100), nullable=True)
    party = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    reelection = Column(Integer, nullable=True)
    promise_completion_percentage = Column(Integer, nullable=True)
    criminal_record = Column(String(100), nullable=True)
    education = Column(String(100), nullable=True)
    property = Column(String(100), nullable=True)
    career = Column(String(100), nullable=True)
    promise = Column(String(100), nullable=True) # todo relation 따로 엮기
    image = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)
    candidate_number = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Candidate {self.name}>"

    def __str__(self):
        return f"<Candidate {self.name}>"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)