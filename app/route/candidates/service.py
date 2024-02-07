"""
Candidate service.
Functions handling business logic should be defined here.
DB operations should be defined in models.
Complicate or multiple ORM operations should be done here
"""
from sqlalchemy.orm import Session

from app.lib.database import with_session, return_response
from app.models.candidates import CandidatesORM
from app.route.candidates.schema import CandidateRegistrationRequest


@with_session
def create_candidate_record(
        body: CandidateRegistrationRequest,
        session=None,
):
    """Create candidate record."""

    CandidatesORM.create(
        **body.__dict__,
        session=session
    )
    return {"SUCCESS"}


@with_session
@return_response
def get_candidate_record(candidate_id: int, session: Session = None):
    """Get candidate record."""
    candidate = CandidatesORM.get(id=candidate_id, session=session)
    return candidate


@with_session
@return_response
def list_candidate_records(session: Session = None):
    """List candidate records."""
    candidates = CandidatesORM.list(session=session)
    return candidates
