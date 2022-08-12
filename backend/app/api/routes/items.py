from typing import Any, Dict, List

from app.api.dependencies.database import get_repository
from app.db.repositories.items import ItemRepository
from app.models.items import Item, ItemCreate, ItemPublic
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

router = APIRouter()


@router.get(
    "/",
    response_model=List[ItemPublic],
    name="itemts:get-items",
    status_code=HTTP_201_CREATED,
)
async def get_all_items(
    items_repo: ItemRepository = Depends(get_repository(ItemRepository)),
) -> List[ItemPublic]:

    items = await items_repo.get_items()
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
async def get_item_by_id(
    id: int, items_repo: ItemRepository = Depends(get_repository(ItemRepository))
) -> ItemPublic:

    item = await items_repo.get_item(id=id)

    if not item:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No item found with id: {id}"
        )

    return item
