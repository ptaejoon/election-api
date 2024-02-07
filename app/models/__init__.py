"""
models classes for sqlalchemy orm
"""
from app.lib.database import engine
from .candidates import *
from .party import *
from .promise import *
from .proposal_records import *
from .district import *
# [TODO] : setting ORM properly

CandidatesORM.metadata.create_all(engine)
CandidatesPromiseRelationORM.metadata.create_all(engine)
PartyORM.metadata.create_all(engine)
PromiseORM.metadata.create_all(engine)
PromiseFriendlinessORM.metadata.create_all(engine)
ProposalRecordsORM.metadata.create_all(engine)
ProposalRecordsCandidateRelationORM.metadata.create_all(engine)
DistrictORM.metadata.create_all(engine)