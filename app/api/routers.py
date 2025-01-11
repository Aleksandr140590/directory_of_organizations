from fastapi import APIRouter

from app.api.endpoints import (
    activities_router,
    buildings_router,
    organizations_router,
)

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
