from enum import Enum
from typing import Optional

from app.models.core import CoreModel, IDModelMixing


# It would be cool to create this model
# based off an external source
class ItemType(str, Enum):
    chicken_bowl = "chicken_bowl"
    chicken_sandwhich = "chicken_sandwich"
    mushroom_skewer = "mushroom_skewer"
    hummus_plate = "hummus_plate"
    crudo = "crudo"


class ItemBase(CoreModel):
    name: Optional[str]
    ingredient: Optional[str]
    price: Optional[float]
    item_type = Optional[ItemType]


class ItemCreate(ItemBase):
    name: str
    price: float


class ItemUpdate(ItemBase):
    item_type: Optional[ItemType]


class ItemModel(IDModelMixing, ItemBase):
    name: str
    price: float
    item_type: ItemType


class ItemPublic(IDModelMixing, ItemBase):
    pass
