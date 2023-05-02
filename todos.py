from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from faker import Faker

app = FastAPI()
fake = Faker()

# A fake database to store items as a dictionary
db = {}

# A Pydantic model to validate the item data
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# A helper function to generate a new item with fake data
def create_item():
    return Item(
        id = len(db) + 1,
        name = fake.word(),
        description = fake.sentence(),
        price = fake.pyfloat(positive=True)
    )

# Populate the database with some initial items
for _ in range(10):
    item = create_item()
    db[item.id] = item

# Create a new item and add it to the database
@app.post("/items/", response_model=Item)
def create_item():
    item = create_item()
    db[item.id] = item
    return item

# Read an item by id
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id in db:
        return db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

# Update an item by id
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id in db:
        db[item_id] = item
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item by id
@app.delete("/items/{item_id}", response_model=None)
def delete_item(item_id: int):
    if item_id in db:
        del db[item_id]
        return None
    raise HTTPException(status_code=404, detail="Item not found")

# Read all items in the database
@app.get("/items/", response_model=List[Item])
def read_items():
    return list(db.values())