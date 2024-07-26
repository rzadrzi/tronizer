from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import UserModel, PartnerModel, APIModel


async def db_init(uri):
    document_models = [UserModel, APIModel]

    tronizer = AsyncIOMotorClient(uri).tronizer

    await init_beanie(database=tronizer, document_models=document_models)
    print("db connected!!!")


