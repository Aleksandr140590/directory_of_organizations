from decimal import Decimal
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from app.core.auth import get_api_key
from app.core.db import get_async_session
from app.crud.organizations import organizations_crud
from app.schemas.organizations import OrganizationBase

router = APIRouter()


@router.get(
    "/search/point1={latitude1},{longitude1}&point2={latitude2},{longitude2}",
    response_model=List[OrganizationBase],
    dependencies=[Depends(get_api_key)],
)
async def get_organizations_in_selected_area(
    latitude1: Decimal,
    longitude1: Decimal,
    latitude2: Decimal,
    longitude2: Decimal,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Ручка получения списка организаций в определенном области заданной двумя координатами
    """
    if (
        latitude1 < -90
        or latitude1 > 90
        or longitude1 < -180
        or latitude1 > 180
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Неверно указаны координаты точки 1"},
        )
    if (
        latitude2 < -90
        or latitude2 > 90
        or longitude2 < -180
        or latitude2 > 180
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Неверно указаны координаты точки 2"},
        )
    organizations = (
        await organizations_crud.get_organizations_in_selected_area(
            (latitude1, longitude1), (latitude2, longitude2), session
        )
    )
    return organizations


@router.get(
    "/search/activity={activity_id}",
    response_model=List[OrganizationBase],
    dependencies=[Depends(get_api_key)],
)
async def get_organizations_by_activities(
    activity_id: int, session: AsyncSession = Depends(get_async_session)
):
    """
    Ручка получения списка организаций определенной сферы деятельности включая вложенные
    """
    organizations = (
        await organizations_crud.get_organizations_with_all_inner_activities(
            activity_id, session
        )
    )
    return organizations


@router.get(
    "/search/name={name}",
    response_model=List[OrganizationBase],
    dependencies=[Depends(get_api_key)],
)
async def get_organizations_by_activities(
    name: str, session: AsyncSession = Depends(get_async_session)
):
    """
    Ручка получения списка организаций по части имени
    """
    organizations = await organizations_crud.get_organizations_by_name(
        name, session
    )
    return organizations


@router.get(
    "/{organization_id}",
    response_model=OrganizationBase,
    dependencies=[Depends(get_api_key)],
)
async def get_organizations_in_building(
    organization_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Ручка получения организации по идентификатору"""
    organization = await organizations_crud.get_organization_by_id(
        organization_id, session
    )
    if organization == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Организация не найдена"},
        )
    return organization
