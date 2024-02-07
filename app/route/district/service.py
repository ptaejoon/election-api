"""
Candidate service.
Functions handling business logic should be defined here.
DB operations should be defined in models.
Complicate or multiple ORM operations should be done here
"""
from typing import List

from sqlalchemy.orm import Session

from app.lib.database import with_session
from app.lib.response import as_dict
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
def get_parent_districts(session: Session = None):
    """Get candidate record."""
    parent_districts = session.query(DistrictORM.parent_district).distinct().all()
    res = []
    for district in parent_districts:
        res.append(district[0])
    return res


@with_session
@as_dict
def get_sub_district(parent_district: str, session: Session = None) -> List[DistrictORM]:
    """Get sub district record."""
    return DistrictORM.list(parent_district=parent_district, session=session)