"""
Candidate service.
Functions handling business logic should be defined here.
DB operations should be defined in models.
Complicate or multiple ORM operations should be done here
"""
from sqlalchemy.orm import Session

from app.lib.database import with_session
from app.models.candidates import CandidatesORM


@with_session
def create_candidate_record(name: str,
                            session=None):
    """Create candidate record."""
    CandidatesORM.create(name=name, session=session)
    return {"SUCCESS"}

@with_session
def get_candidate_record(candidate_id: int, session: Session = None):
    """Get candidate record."""
    candidate = CandidatesORM.get(id=candidate_id, session=session)
    return candidate