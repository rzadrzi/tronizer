
from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.web.database.database_config import db_init
from routes import user_router, api_router, customer_router
from config import Settings


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Welcome to Tronizer")
    global uri
    settings = Settings()

    if settings.MODE == "local":
        uri = settings.MONGO_LOCAL_URI
    elif settings.MODE == "docker":
        uri = settings.MONGO_DOCKER_URI

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
