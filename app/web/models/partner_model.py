import pymongo
from beanie import Document, Link
from pydantic import Field
from pymongo import IndexModel

from models import UserModel, APIModel


class PartnerModel(Document):
    user: Link[UserModel] = Field(default=None)
    api: Link[APIModel] = Field(default=None)
    permission: bool = Field(default=False)

    class Settings:
        name = "partners"
        indexes = [
            IndexModel([("user", pymongo.ASCENDING), ("api", pymongo.ASCENDING)], unique=True)
        ]
