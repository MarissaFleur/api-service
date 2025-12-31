from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    user: User

items = [
    {"id": 1, "title": "Item 1", "description": "This is item 1", "price": 10.99},
    {"id": 2, "title": "Item 2", "description": "This is item 2", "price": 20.99},
    {"id": 3, "title": "Item 3", "description": "This is item 3", "price": 30.99}
]

@app.get("/")
async def read_root():
    return {"message": "Welcome to API Service"}

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items/")
async def create_item(item: Item):
    items.append(item.dict())
    return item