# import necessary libraries
from fastapi import FastAPI, HTTPException
from firebase_admin import firestore
from pydantic import BaseModel

# import firebase database loaded in db.py
from db import db

# initiate FastAPI
app = FastAPI()

# Check input data type by Pydantic
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Add a data point in items collection
@app.post("/items/")
async def create_item(item: Item):
    doc_ref = db.collection("items").document()
    doc_ref.set(item.model_dump())
    return {"id": doc_ref.id}

# Read a data point in items collection by id
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Update a data point in items collection by id 
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.update(item.model_dump())
        return {"message": "Item updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Delete a data point in items collection by id
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
