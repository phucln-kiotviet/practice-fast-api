# FastAPI

- From official [doc](https://fastapi.tiangolo.com/)


## Muc luc
- Finished: 
  - [Project generation](https://fastapi.tiangolo.com/project-generation/)

- Also in progress: [SQL Database](https://fastapi.tiangolo.com/tutorial/sql-databases/): Stop at this: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-data
- Stop [at](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) --> Continue after it

## Env

- Create virtual env:

```shell
python3 -m venv venv
```

- Active venv:

```shell
source venv/bin/activate
```

- Install package
```shell
pip3 install <package_name>
```

- Install from `requirements.txt`
```shell
pip3 install -r requirements.txt
```

## Install package
- Install fastapi package:

```
pip install "fastapi[all]"
```

- If you need a ASGI server, for production use [Uvicorn](https://www.uvicorn.org/) or [Hypercorn](https://github.com/pgjones/hypercorn)
```
pip install "uvicorn[standard]"
```


## Run server
- Run server

```shell
uvicorn main:app --reload
```

- Check doc at: `localhost:8000/docs` 

- Check other doc at: `localhost:8000/redoc`

## Request body

- Function parameters will be recognized as follows:
  - Nếu param được khai báo trong `path` nó sẽ là `path parameters`.
  - Nếu param là `single type` ( như `int`, `float`, `str`, `bool`) nó sẽ được hiểu `query` parameters.
  - Nếu param được khai báo kiểu `pydantic model` sẽ được dịch là request body.

## SQLAlchemy model vs Pydantic model

- To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file `models.py` with the SQLAlchemy models and the file `schemas.py` with the Pydantic models.

- SQLAlchemy style and Pydantic style: SQLAlchemy using `=` and pass type as param to `Column` like: `name = Column(String)` while Pydantic models declare the types using `:`, the new type annotation syntax/type hints: `name: str`. Have it in mind!!!

- Pydantic's `orm_mode` tell Pydantic model to read the data even if it is not a `dict`, but an ORM model ( or any other arbitrary object with attributes).

