from fastapi import FastAPI

from app.api.routes import assignments
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(assignments.router, prefix=settings.API_V1_STR)
