from fastapi import FastAPI, Depends, HTTPException, Body, Request
from fastapi.templating import Jinja2Templates
from schema import Item, ItemResponse, DeleteResponse
from model import Base, ItemDB
from database import engine, get_db
from sqlalchemy.orm import Session


#-- Initialize FastAPI app
app = FastAPI(title="FastAPI User App", version="1.0.0")

#-- Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

#-- Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")


# ── HTML Pages ─────────────────────────────────────────────────────────────

@app.get("/")
def read_root(request: Request):
    endpoints = [
        {"method": "GET",    "route": "/items/all",                   "desc": "Get all items",             "page": "/page/all"},
        {"method": "GET",    "route": "/items/{item_id}",             "desc": "Get item by ID",            "page": ""},
        {"method": "GET",    "route": "/items/search?column=&value=", "desc": "Search items by column",    "page": "/page/search"},
        {"method": "POST",   "route": "/items",                       "desc": "Create one or more items",  "page": "/page/create"},
        {"method": "DELETE", "route": "/items/{item_id}",             "desc": "Delete item by ID",         "page": "/page/delete"},
    ]
    return templates.TemplateResponse(request, "index.html", {"endpoints": endpoints})


@app.get("/page/all")
def page_all(request: Request, db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    return templates.TemplateResponse(request, "all_items.html", {"items": items})


@app.get("/page/search")
def page_search(request: Request, column: str = None, value: str = None, db: Session = Depends(get_db)):
    items = None
    if column and value:
        column_map = {
            "name": ItemDB.name, "description": ItemDB.description,
            "note": ItemDB.note, "date_posted": ItemDB.date_posted, "price": ItemDB.price
        }
        items = db.query(ItemDB).filter(column_map[column] == value).all() if column in column_map else []
    return templates.TemplateResponse(request, "search.html", {"items": items, "column": column, "value": value})


@app.get("/page/create")
def page_create(request: Request):
    return templates.TemplateResponse(request, "create.html", {})


@app.get("/page/delete")
def page_delete(request: Request):
    return templates.TemplateResponse(request, "delete.html", {})


# ── API Endpoints ───────────────────────────────────────────────────────────

@app.get("/items/all", response_model=list[ItemResponse])
def read_all(db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    return items


@app.get("/items/search", response_model=list[ItemResponse])
def read_items(column: str, value: str, db: Session = Depends(get_db)):
    column_map = {
        "name": ItemDB.name,
        "description": ItemDB.description,
        "note": ItemDB.note,
        "date_posted": ItemDB.date_posted,
        "price": ItemDB.price
    }
    if column not in column_map:
        raise HTTPException(status_code=400, detail=f"Invalid column. Choose from: {list(column_map.keys())}")
    items = db.query(ItemDB).filter(column_map[column] == value).all()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items


@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=list[ItemResponse])
def create_item(items: list[Item] = Body(...), db: Session = Depends(get_db)):
    db_items = [
        ItemDB(
            id=item.id,
            name=item.name,
            price=item.price,
            description=item.description,
            note=item.Note,
            date_posted=item.date_posted
        ) for item in items
    ]
    db.add_all(db_items)
    db.commit()
    for db_item in db_items:
        db.refresh(db_item)
    return db_items


@app.delete("/items/{item_id}", response_model=DeleteResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully", "item": item}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
