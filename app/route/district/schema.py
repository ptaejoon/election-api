from pydantic import BaseModel
from typing import Optional

class DistrictRegistrationRequest(BaseModel):
    parent_district: Optional[str] = None
    name: str