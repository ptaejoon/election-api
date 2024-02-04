from pydantic import BaseModel
from typing import Optional

class DistrictRegisterRequest(BaseModel):
    parent_district: Optional[str] = None
    name: str