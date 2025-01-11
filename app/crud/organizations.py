from decimal import Decimal
from typing import Optional, List

from sqlalchemy import select, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.utils import collect_inner_activity_ids
from app.models.buildings import Building
from app.models.organizations import (
    Organization,
    Activity,
    OrganizationActivity,
)


class CRUDOrganization:

    async def get_organization_in_building(
        self, building_id: int, session: AsyncSession
    ) -> Optional[list[Organization]]:
        """Получение из БД всех организаций в определенном здании."""
        organizations = await session.execute(
            select(Organization).where(Organization.building_id == building_id)
        )
        organizations = self.collect_phone_numbers(
            organizations.scalars().all()
        )
        return organizations

    @staticmethod
    def collect_phone_numbers(
        organizations: List[Organization] | Organization,
    ) -> List[Organization]:
        for organization in organizations:
            if organization.phones:
                organization.phone_numbers = [
                    phone.phone_number for phone in organization.phones
                ]
        return organizations

    async def get_organization_by_activity(
        self, activity_id: int, session: AsyncSession
    ) -> Optional[list[Organization]]:
        """Получение из БД всех организаций с определенным видом деятельности."""
        organizations = await session.execute(
            select(Organization)
            .join(OrganizationActivity)
            .join(Activity)
            .where(Activity.id == activity_id)
        )
        organizations = self.collect_phone_numbers(
            organizations.scalars().all()
        )
        return organizations

    async def get_organization_by_id(
        self, organization_id: int, session: AsyncSession
    ) -> Optional[Organization]:
        """Получение из БД организации по ее идентификатору."""
        organization = await session.execute(
            select(Organization).where(Organization.id == organization_id)
        )
        organization = organization.scalars().first()
        if organization and organization.phones:
            organization.phone_numbers = [
                phone.phone_number for phone in organization.phones
            ]
        return organization

    async def get_organizations_in_selected_area(
        self,
        point1: tuple[Decimal],
        point2: tuple[Decimal],
        session: AsyncSession,
    ) -> List[Organization]:
        """Получение из БД организации находящихся в области ограниченной 2-мя точками"""
        organizations = await session.execute(
            select(Organization)
            .join(Building)
            .where(
                and_(
                    or_(
                        and_(
                            point1[0] <= Building.latitude,
                            Building.latitude <= point2[0],
                        ),
                        and_(
                            point2[0] <= Building.latitude,
                            Building.latitude <= point1[0],
                        ),
                    ),
                    or_(
                        and_(
                            point1[1] <= Building.longitude,
                            Building.longitude <= point2[1],
                        ),
                        and_(
                            point2[1] <= Building.longitude,
                            Building.longitude <= point1[1],
                        ),
                    ),
                )
            )
        )

        organizations = self.collect_phone_numbers(
            organizations.scalars().all()
        )
        return organizations

    async def get_organizations_with_all_inner_activities(
        self, activity_id: int, session: AsyncSession
    ) -> List[Organization]:
        """Получение из БД организаций с определенной сферой деятельности и вложенные в нее"""
        activity = await session.execute(
            select(Activity)
            .options(
                selectinload(Activity.inner_activities, recursion_depth=2)
            )
            .where(Activity.id == activity_id)
        )
        activity = activity.scalars().first()
        activity_ids = collect_inner_activity_ids(activity)
        organizations = await session.execute(
            select(Organization)
            .join(OrganizationActivity)
            .join(Activity)
            .where(Activity.id.in_(activity_ids))
        )
        organizations = self.collect_phone_numbers(
            organizations.scalars().all()
        )
        return organizations

    async def get_organizations_by_name(
        self, name: str, session: AsyncSession
    ) -> List[Organization]:
        """Получение из БД организаций по части имени"""
        organizations = await session.execute(
            select(Organization).where(Organization.name.icontains(name))
        )
        organizations = self.collect_phone_numbers(
            organizations.scalars().all()
        )
        return organizations


organizations_crud = CRUDOrganization()
