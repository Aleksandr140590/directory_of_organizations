from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette import status
from starlette.responses import JSONResponse

from app.api.endpoints import (
    activities_router,
    buildings_router,
    organizations_router,
)
from app.core.db import get_async_session
from app.models.organizations import Activity
from app.utils.test_data import test_data1, test_data2

main_router = APIRouter()
main_router.include_router(
    buildings_router, prefix="/buildings", tags=["Здания"]
)
main_router.include_router(
    activities_router, prefix="/activities", tags=["Деятельность"]
)
main_router.include_router(
    organizations_router, prefix="/organizations", tags=["Организации"]
)


@main_router.post("/", response_model=None, tags=["Тестовые данные"])
async def upload_test_data(session: AsyncSession = Depends(get_async_session)):
    """Загрузка тестовых данных"""
    try:
        activity = await session.execute(select(Activity))
        if activity.scalars().first():
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": "БД не пуста"},
            )
        session.add_all(test_data1)
        await session.commit()
        session.add_all(test_data2)
        await session.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Данные загружены"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Данные уже были загружены или что то пошло не так"
            },
        )
