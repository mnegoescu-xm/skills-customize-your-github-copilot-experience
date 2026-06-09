from typing import Optional, Dict, List
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
import logging

app = FastAPI(title="Mergington API", version="1.0.0", description="Production-minded API examples")
logger = logging.getLogger("uvicorn")

class Settings(BaseModel):
    app_name: str = "Mergington API"

def get_settings():
    return Settings()

class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., example="Widget")
    description: Optional[str] = Field(None, example="A useful widget")
    price: float = Field(..., gt=0, example=9.99)

# Simple in-memory repository
class Repo:
    def __init__(self):
        self._items: Dict[int, Item] = {}
        self._next = 1

    def list(self) -> List[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Optional[Item]:
        return self._items.get(item_id)

    def create(self, item: Item) -> Item:
        item.id = self._next
        self._items[self._next] = item
        self._next += 1
        return item

    def update(self, item_id: int, item: Item) -> Item:
        item.id = item_id
        self._items[item_id] = item
        return item

    def delete(self, item_id: int):
        del self._items[item_id]

repo = Repo()

@app.on_event("startup")
def startup_event():
    logger.info("Starting Mergington API...")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down Mergington API...")

@app.get("/items", response_model=List[Item], summary="List items")
def list_items(settings: Settings = Depends(get_settings)):
    return repo.list()

@app.get("/items/{item_id}", response_model=Item, summary="Get an item")
def get_item(item_id: int):
    item = repo.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, summary="Create an item")
def create_item(item: Item):
    created = repo.create(item)
    return created

@app.put("/items/{item_id}", response_model=Item, summary="Update an item")
def update_item(item_id: int, item: Item):
    if not repo.get(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return repo.update(item_id, item)

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an item")
def delete_item(item_id: int):
    if not repo.get(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    repo.delete(item_id)
    return None
