from datetime import datetime
from typing import Optional

from beanie import Document, Link
from pydantic import Field

from web import PartnerModel
from schema import WithdrawalStatus


class WithdrawalModel(Document):
    """
    Withdrawal model for using transaction on database
    use beanie library
    """
    network: Optional[str] = Field(default="TRON")
    partner: Link[PartnerModel]
    amount: float = Field(default=0.00)
    to: str = Field(default=None) # Wallet public key
    status: WithdrawalStatus = Field(default=WithdrawalStatus.fail)
    txid: str = Field(default="")
    create_at: float = Field(default=datetime.now().timestamp())
    update_at: float = Field(default=datetime.now().timestamp())