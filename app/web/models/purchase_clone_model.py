from beanie import Document, Link

from models import PurchaseModel


class PurchaseCloneModel(Document):
    purchase_clone_model = Link[PurchaseModel]

    class Settings:
        name = "purchase_clones"
