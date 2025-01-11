import re
from typing import List

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from app.core.db import Base
from app.models.buildings import Building


class Activity(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    parent_id = Column(
        Integer, ForeignKey("activity.id"), nullable=True, default=None
    )
    inner_activities = relationship(
        "Activity", back_populates="parent_activity"
    )
    parent_activity = relationship(
        "Activity", back_populates="inner_activities", remote_side=[id]
    )
    organizations = relationship(
        "Organization",
        secondary="organizationactivity",
        back_populates="activities",
    )

    def __repr__(self):
        return self.name


class OrganizationActivity(Base):
    organization_id = Column(
        Integer, ForeignKey("organization.id"), nullable=False
    )
    activity_id = Column(Integer, ForeignKey("activity.id"), nullable=False)


class Organization(Base):
    name = Column(String(300), nullable=False)
    phones = relationship("OrganizationPhoneNumber", lazy="selectin")
    activities = relationship(
        "Activity",
        secondary="organizationactivity",
        back_populates="organizations",
        lazy="selectin",
    )
    building_id = Column(Integer, ForeignKey("building.id"), nullable=False)
    building = relationship(
        Building, back_populates="organizations", lazy="selectin"
    )


class OrganizationPhoneNumber(Base):
    organization_id = Column(
        Integer, ForeignKey("organization.id"), nullable=False
    )
    phone_number = Column(String(300), nullable=False)

    def validate_phone_number(self, phone_number):
        if re.match("^[0-9\\-()]{1,15}$", phone_number):
            return phone_number
        return ValueError("Invalid phone number")
