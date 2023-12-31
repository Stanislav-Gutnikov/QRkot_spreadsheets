from fastapi import APIRouter # noqa

from app.api.endpoints.charity_project import router as charity_projects_router
from app.api.endpoints.donation import router as donations_router
from app.api.endpoints.user import router as user_router
from app.api.endpoints.google_api import router as google_api_router


main_router = APIRouter()
main_router.include_router(charity_projects_router)
main_router.include_router(donations_router)
main_router.include_router(google_api_router)
main_router.include_router(user_router)
