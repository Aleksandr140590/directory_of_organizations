from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.organizations import organizations_crud
from app.schemas.organizations import OrganizationBase

router = APIRouter()


@router.get("/{activity_id}", response_model=List[OrganizationBase])
async def get_organizations_in_building(
    activity_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Cписок всех организаций, которые относятся к указанному виду деятельности"""
    organizations = await organizations_crud.get_organization_by_activity(
        activity_id, session
    )
    return organizations
