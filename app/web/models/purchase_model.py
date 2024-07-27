from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from beanie import Document, Link
from pydantic import Field

from models import APIModel, WalletModel
from schema import PurchaseStatus


class PurchaseModel(Document):
    """
    Purchase model for using transaction on database
    use beanie library
    """
    network: Optional[str] = Field(default="TRON")
    purchase_token: Optional[str] = Field(default=uuid4().hex)
    api: Link[APIModel] = Field(default=None)
    wallet: Optional[Link[WalletModel]] = Field(default=None)
    amount: float = Field(default=0.00)
    balance: float = Field(default=0.00)
    is_open: bool = Field(default=True)
    confirmed: bool = Field(default=False)
    status: PurchaseStatus = Field(default=PurchaseStatus.fail)
    create_at: float = Field(default=datetime.now().timestamp())
    update_at: float = Field(default=datetime.now().timestamp())
    expiration_at: float = Field(default=(datetime.now()+timedelta(minutes=30)).timestamp())

    class Settings:
        name = "purchases"
