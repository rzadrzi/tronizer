from typing import Optional

from beanie import Document
from pydantic import Field


class WalletModel(Document):
    """
    Wallet model for using wallet on database
    use beanie library
    """
    network: Optional[str] = Field(default="TRON")
    public_key: str
    private_key: str
    balance: float = Field(default=0.00)
    in_order: bool = Field(default=False)

    class Settings:
        name = "wallets"
