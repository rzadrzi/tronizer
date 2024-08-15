from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from beanie import Document, Link
from pydantic import Field

from models import PurchaseModel


class PurchasePageModel(Document):
    purchase: Link[PurchaseModel]
    create_at: float = Field(default=datetime.now().timestamp())
    update_at: float = Field(default=datetime.now().timestamp())
    expiration_at: float = Field(default=(datetime.now()+timedelta(minutes=5)).timestamp())

    class Settings:
        name = "purchase_pages"
