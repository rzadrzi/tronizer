import asyncio

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
# from models import UserModel
# from web.models.user_model import UserModel
from datetime import datetime
from typing import Optional
from uuid import uuid4

import pymongo
from beanie import Document, Indexed
from pydantic import Field


class UserModel(Document):
    """
    User model for using user on database
    use beanie library
    """
    user_id: Optional[str] = Field(default=uuid4().hex)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    email: Indexed(str, unique=True)
    is_verified: bool = Field(default=False)
    total_balance: Optional[float] = Field(default=0.00)
    create_at: float = Field(default=datetime.now().timestamp())
    update_at: float = Field(default=datetime.now().timestamp())

    class Settings:
        name = "users"
        indexes = [
            [
                ("email", pymongo.TEXT)
            ]
        ]


async def db_init(uri):
    print("welcome to database")
    document_models = [UserModel]
    tronizer = AsyncIOMotorClient(uri).tronizer
    await init_beanie(database=tronizer, document_models=document_models)
    print("db connected!!!")


if __name__=="__main__":
    asyncio.run(db_init("mongodb://127.0.0.1:27017"))