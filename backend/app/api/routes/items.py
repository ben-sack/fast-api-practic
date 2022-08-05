from typing import Any, Dict, List

from fastapi import APIRouter

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
