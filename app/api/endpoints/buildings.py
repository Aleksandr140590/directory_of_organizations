from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_api_key
from app.core.db import get_async_session
from app.crud.organizations import organizations_crud
from app.schemas.organizations import OrganizationBase

router = APIRouter()


@router.get(
    "/{building_id}",
    response_model=List[OrganizationBase],
    dependencies=[Depends(get_api_key)],
)
async def get_organizations_in_building(
    building_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Cписок всех организаций находящихся в конкретном здании"""
    organizations = await organizations_crud.get_organization_in_building(
        building_id, session
    )
    return organizations
