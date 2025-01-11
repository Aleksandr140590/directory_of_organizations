from pydantic import BaseModel
from typing import Optional, List

from app.schemas.activities import OrganizationActivityBase
from app.schemas.buildings import BuildingBase


class OrganizationBase(BaseModel):
    name: str
    phone_numbers: Optional[List[str]]
    activities: Optional[List[OrganizationActivityBase]]
    building: BuildingBase
