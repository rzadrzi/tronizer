# import app.libs
import sys
print(sys.path)
from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.web.database.database_config import db_init
from routes import user_router, api_router, customer_router


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
app.include_router(customer_router)
