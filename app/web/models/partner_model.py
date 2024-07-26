from beanie import Document, Link
from pydantic import Field
from models import UserModel, APIModel
import pymongo
from pymongo import IndexModel


class PartnerModel(Document):
    user: Link[UserModel] = Field(default=None)
    api: Link[APIModel] = Field(default=None)
    permission: bool = Field(default=False)


    class Settings:
        name = "partners"
        indexes = [
            IndexModel([("user", pymongo.ASCENDING), ("api", pymongo.ASCENDING)], unique=True)
        ]
