from enum import Enum
from typing import Optional

from app.models.core import CoreModel, IDModelMixing


class ItemType(str, Enum):
    pass


class ItemBase(CoreModel):
    """
    All common characteristics of Item resource
    """

    name: Optional[str]
    ingredient: Optional[str]
    price: Optional[int]
