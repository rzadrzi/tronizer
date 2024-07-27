from beanie import Document, Link

from models import PurchaseModel


class PurchaseCloneModel(Document):
    purchase = Link[PurchaseModel]

    class Settings:
        name = "purchase_clones"
