import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None



app = FastAPI()

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)



@app.post("/items")
async def create_item(item: Item):
  return item
