import uvicorn
from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, Query

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None



app = FastAPI()

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)



# @app.post("/items")
# async def create_item(item: Item):
#   item_dict = item.dict()
#   if item.tax:
#     price_with_tax = item.price + item.tax
#     item_dict.update({"price_with_tax": price_with_tax})
#   return item_dict

# @app.put("/items")
# async def create_item(item_id: int, item: Item):
#   return {"item_id": item_id, **item.dict()}

@app.get("/items")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
  results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q": q})
  return results