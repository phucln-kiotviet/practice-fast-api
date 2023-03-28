# FastAPI

- From official [doc](https://fastapi.tiangolo.com/)

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

