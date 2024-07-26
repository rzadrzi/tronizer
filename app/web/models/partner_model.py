from beanie import Document, Link
from pydantic import Field

from models import UserModel


class PartnerModel(Document):
    user: Link[UserModel] = Field(default=None)
    permission: bool = Field(default=False)

    class Settings:
        name = "partners"