import app.libs
from fastapi import FastAPI

from contextlib import asynccontextmanager
from web.database import db_init
from web.routes import user_router, api_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Welcome to Tronizer")
    uri = "mongodb://127.0.0.1:27017"
    await db_init(uri)

    yield


app = FastAPI(
    title="Tronizer",
    version="0.0.13",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(api_router)
