from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.lib.database import configure_sqlalchemy
from app.route.candidates import candidates_router
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # When app starts
    
    yield
    # When app teardown
_db_uri = "mysql+pymysql://roly:rolypoly@localhost:3306/election"

configure_sqlalchemy(
    connection_uri=_db_uri,
    engine_options={
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 3600,
    },
)


app.include_router(candidates_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

