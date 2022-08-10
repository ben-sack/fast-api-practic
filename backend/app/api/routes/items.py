from typing import Any, Dict, List

from app.api.dependencies.database import get_repository
from app.db.repositories.items import ItemRepository
from app.models.items import Item, ItemCreate, ItemPublic
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

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


@router.get("/{id}/", response_model=ItemPublic, name="items:get-item")
async def get_item(
    id: int,
    items_repo: ItemRepository = Depends(get_repository(ItemRepository)) 
) -> ItemPublic:
    
    item = await items_repo.get_item(id=id)
    
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"No item found with id: {id}")
    
    return item
