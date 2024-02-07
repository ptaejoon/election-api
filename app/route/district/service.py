"""
Candidate service.
Functions handling business logic should be defined here.
DB operations should be defined in models.
Complicate or multiple ORM operations should be done here
"""
from sqlalchemy.orm import Session

from app.lib.database import with_session
from app.models.candidates import CandidatesORM
from app.models.district import DistrictORM
from app.route.district.schema import DistrictRegistrationRequest

@with_session
def create_district(
                            body: DistrictRegistrationRequest,
                            session=None,
                            ):
    """Create candidate record."""

    DistrictORM.create(
        **body.__dict__,
        session=session
    )
    return {"SUCCESS"}


@with_session
def get_district_record(district_id: int, session: Session = None):
    """Get candidate record."""


@with_session
def get_sub_district(parent_district: str, session: Session = None):
    """Get sub district record."""
    return DistrictORM.get(parent_district=parent_district, session=session)