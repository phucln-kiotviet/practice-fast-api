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
pip install fastapi
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