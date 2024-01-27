from pydantic import BaseModel
from typing import Optional

class CandidateRegistrationRequest(BaseModel):
    party: Optional[str] = None
    age: int
    district: str
    name: str
    property: str
    address: Optional[str] = None
    criminal_record: Optional[str] = None
    education: Optional[str] = None
    career: Optional[str] = None
    promise: Optional[str] = None
    image: Optional[str] = None
