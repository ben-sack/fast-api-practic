from app.api.routes.items import router as items_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(items_router, prefix="/items", tags=["items"])
