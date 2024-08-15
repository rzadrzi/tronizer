import os

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from config import Settings
from database import db_init
from routes import user_router, api_router, customer_router
from scheduler import collector_scheduler, balance_scheduler


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

    await collector_scheduler()
    await balance_scheduler()

    yield


app = FastAPI(
    title="Tronizer",
    version="0.0.13",
    lifespan=lifespan
)
static_path = str(os.path.join(os.getcwd(), "app", "web", "templates", "static"))
app.mount("/static", StaticFiles(directory=static_path), name="static")
templates_path = str(os.path.join(os.getcwd(), "app", "web", "templates"))
print(templates_path)
templates = Jinja2Templates(directory=templates_path)


@app.get("/purchase", response_class=HTMLResponse)
async def purchase_query_get(request: Request):
    return templates.TemplateResponse(request=request, name="qrcode.html")


app.include_router(user_router)
app.include_router(api_router)
app.include_router(customer_router)
