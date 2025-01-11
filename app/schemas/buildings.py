from decimal import Decimal

from pydantic import BaseModel
from sqlalchemy import Numeric


class BuildingBase(BaseModel):
    id: int
    address: str
    latitude: Decimal
    longitude: Decimal
