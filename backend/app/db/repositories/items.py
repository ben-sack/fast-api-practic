from app.db.repositories.base import BaseRepository
from app.models.items import Item, ItemCreate, ItemUpdate

CREATE_ITEM_QUERY = """
    INSERT INTO items (name, price, item_type)
    VALUES (:name, :price, :item_type)
    RETURNING id, name, price, item_type;
"""


class ItemRepository(BaseRepository):
    """
    All database actions associated with the Item resource
    """

    async def create_item(self, *, new_item: ItemCreate) -> Item:
        query_values = new_item.dict()
        item = await self.db.fetch_one(query=CREATE_ITEM_QUERY, values=query_values)
        return Item(**item)
