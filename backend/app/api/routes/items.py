from typing import Any, Dict, List

from app.api.dependencies.database import get_repository
from app.db.repositories.items import ItemRepository
from app.models.items import ItemCreate, ItemPublic, Item
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED


router = APIRouter()


@router.get("/")
async def get_all_items() -> List[Dict[str, Any]]:
    items = [
        {
            "id": 1,
            "name": "Chicken Bowl",
            "ingredients": ["chicken", "rice", "sesame seeds", "peri peri"],
            "price": 17,
        },
        {
            "id": 2,
            "name": "Mushroom Skewer",
            "ingredients": ["portabello mushroom"],
            "price": 12,
        },
    ]
    return items


@router.post(
    "/",
    response_model=ItemPublic,
    name="items:create-item",
    status_code=HTTP_201_CREATED,
)
async def create_new_item(
    new_item: ItemCreate = Body(..., embed=True),
    items_repo: ItemRepository = Depends(get_repository(ItemRepository)),
) -> ItemPublic:
    created_item = await items_repo.create_item(new_item=new_item)
    return created_item
