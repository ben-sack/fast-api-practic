from enum import Enum
from typing import Optional

from app.models.core import CoreModel, IDModelMixin


# It would be cool to create this model
# based off an external source
class ItemType(str, Enum):
    meat = "meat"
    vegitarien = "vegitarien"
    drink = "drink"
    desert = "desert"
    dairy = "dairy"


class ItemBase(CoreModel):
    name: Optional[str]
    ingredients: Optional[str]
    price: Optional[float]
    item_type: Optional[ItemType]


class ItemCreate(ItemBase):
    name: str
    price: float


class ItemUpdate(ItemBase):
    item_type: Optional[ItemType]


class Item(IDModelMixin, ItemBase):
    name: str
    price: float
    item_type: ItemType


class ItemPublic(IDModelMixin, ItemBase):
    pass
