"""
proposal_records
"""

from sqlalchemy import Integer, Column, String

from app.models import BaseORM


class ProposalRecordsCandidateRelationORM(BaseORM):
    __tablename__ = "proposal_records_candidate_relation"
    id = Column(Integer, primary_key=True)
    proposal_id = Column(Integer)
    candidate_id = Column(Integer)


class ProposalRecordsORM(BaseORM):
    __tablename__ = "proposal_records"
    id = Column(Integer, primary_key=True)
    proposal = Column(String(500))
    proposal_date = Column(String(100))
