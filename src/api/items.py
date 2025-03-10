from fastapi import APIRouter, Depends, HTTPException, Query
from ..models.item import Item, ItemCreate, ItemUpdate
from ..models.user import User
from ..services.auth import get_current_user
from typing import List, Optional

router = APIRouter()

# Example in-memory database
fake_items_db = [
    {"id": 1, "name": "Item 1", "description": "Description 1", "owner_id": 1},
    {"id": 2, "name": "Item 2", "description": "Description 2", "owner_id": 1},
    {"id": 3, "name": "Item 3", "description": "Description 3", "owner_id": 2},
]

@router.get("/", response_model=List[Item])
async def read_items(
    skip: int = 0, 
    limit: Optional[int] = Query(10, le=100),
    current_user: User = Depends(get_current_user)
):
    return fake_items_db[skip : skip + limit]

@router.get("/{item_id}", response_model=Item)
async def read_item(
    item_id: int, 
    current_user: User = Depends(get_current_user)
):
    item = next((i for i in fake_items_db if i["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item, status_code=201)
async def create_item(
    item: ItemCreate,
    current_user: User = Depends(get_current_user)
):
    # Generate new ID (would use DB sequence in real app)
    new_id = max(i["id"] for i in fake_items_db) + 1 if fake_items_db else 1
    
    # Create and add new item
    new_item = {
        "id": new_id,
        "name": item.name,
        "description": item.description,
        "owner_id": current_user.id,
    }
    fake_items_db.append(new_item)
    return new_item

@router.put("/{item_id}", response_model=Item)
async def update_item(
    item_id: int,
    item: ItemUpdate,
    current_user: User = Depends(get_current_user)
):
    # Find item in DB
    item_index = next((i for i, item in enumerate(fake_items_db) 
                      if item["id"] == item_id), None)
    
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Check ownership
    if fake_items_db[item_index]["owner_id"] != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this item")
    
    # Update item with new values, keeping existing values for None fields
    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            fake_items_db[item_index][key] = value
    
    return fake_items_db[item_index]

@router.delete("/{item_id}", status_code=204)
async def delete_item(
    item_id: int,
    current_user: User = Depends(get_current_user)
):
    # Find item in DB
    item_index = next((i for i, item in enumerate(fake_items_db) 
                      if item["id"] == item_id), None)
    
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Check ownership
    if fake_items_db[item_index]["owner_id"] != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this item")
    
    # Remove the item
    del fake_items_db[item_index]