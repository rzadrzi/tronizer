from beanie import Document
from pydantic import Field
from models import UserModel


class PartnerModel(Document):
    user: UserModel = Field(default=None)
    permission: bool = Field(default=False)

    class Settings:
        name = "partners"