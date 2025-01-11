from sqlalchemy import (
    Column,
    String,
    Numeric,
    CheckConstraint,
    UniqueConstraint,
)
from sqlalchemy.orm import validates, relationship

from app.core.db import Base


class Building(Base):
    address = Column(String(300), nullable=False)
    latitude = Column(
        Numeric(8, 6),
        CheckConstraint("latitude > -90 AND latitude < 90"),
        nullable=False,
    )
    longitude = Column(
        Numeric(9, 6),
        CheckConstraint("longitude > -180 AND longitude < 180"),
        nullable=False,
    )
    organizations = relationship("Organization", back_populates="building")
    __table_args__ = (
        UniqueConstraint(
            "latitude", "longitude", name="_building_location_uc"
        ),
    )

    def __repr__(self):
        return self.address

    @validates("latitude")
    def validate_latitude(self, key, value):
        if -90 <= value <= 90:
            return value
        return ValueError("latitude must be between -90 and 90")

    @validates("longitude")
    def validate_longitude(self, key, value):
        if -180 <= value <= 180:
            return value
        return ValueError("longitude must be between -180 and 180")
