from enum import Enum

from pydantic import Field, BaseModel


class PurchaseStatus(str, Enum):
    fail = "FAIL"
    less = "LESS"
    success = "SUCCESS"


class WithdrawalStatus(str, Enum):
    fail = "FAIL"
    success = "SUCCESS"


class AddPartner(BaseModel):
    user_id: str
    api_key: str
    permission: bool = Field(default=False)


class UserSchema(BaseModel):
    username: str
    password: str
    phone_number: str
    email: str


class APISchema(BaseModel):
    user_id: str
    url: str


class WithdrawalSchema(BaseModel):
    to: str = Field(default=None)
    amount: float = Field(default=None)


class PaymentSchema(BaseModel):
    amount: float = Field(default=None)