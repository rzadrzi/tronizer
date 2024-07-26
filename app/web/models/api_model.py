from datetime import datetime
from typing import Optional, List
from uuid import uuid4

from beanie import Document, Indexed, Link
from pydantic import Field

from models import UserModel, PartnerModel


class APIModel(Document):
        """
        User model for using user on database
        use beanie library
        """
        api_key: Optional[str] = Field(default=uuid4().hex)
        owner: Link[UserModel]
        url: str
        domain: Indexed(str, unique=True)
        partner: Optional[List[Link[PartnerModel]]] = Field(default=None)
        balance: Optional[float] = Field(default=0.00)
        create_at: float = Field(default=datetime.now().timestamp())
        update_at: float = Field(default=datetime.now().timestamp())

        class Settings:
                name = 'apis'
