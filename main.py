import uvicorn
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)



@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
  if q:
    return {"item_id": item_id, "q": q}
  return {"item_id": item_id}
