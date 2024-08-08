
from datetime import datetime

from beanie import Document, Link
from pydantic import Field

from models import PurchaseModel
from schema import PurchaseStatus


class PurchaseCloneModel(Document):
    purchase: Link[PurchaseModel]
    status: PurchaseStatus = Field(default=PurchaseStatus.fail)
    create_at: float = Field(default=datetime.now().timestamp())
    update_at: float = Field(default=datetime.now().timestamp())

    class Settings:
        name = "purchase_clones"
