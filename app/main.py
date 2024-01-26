from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.route.candidates import candidates_router
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # When app starts
    
    yield
    # When app teardown
    
app.include_router(candidates_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

