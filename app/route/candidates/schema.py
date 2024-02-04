from pydantic import BaseModel
from typing import Optional

class CandidateRegistrationRequest(BaseModel):
    name: str
    chinese_name: Optional[str] = None
    party: str
    age: str
    address: Optional[str] = None
    reelection: Optional[int] = None
    promise_completion_percentage: Optional[int] = None
    criminal_record: Optional[str] = None
    education: Optional[str] = None
    property: Optional[str] = None
    career: Optional[str] = None
    promise: Optional[str] = None
    image: Optional[str] = None
    district: str
    candidate_number: Optional[int] = None
    job: Optional[str] = None
    gender: str