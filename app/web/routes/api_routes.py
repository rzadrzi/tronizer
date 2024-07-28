from typing import Annotated
from fastapi import APIRouter, Header, HTTPException

from controllers import APIController, WithdrawalController
from schema import APISchema, AddPartner, WithdrawalSchema


api_router = APIRouter(
    prefix="/api"
)


@api_router.post("/create")
async def create_api(api: APISchema):
    api_ctrl = APIController()
    api_key = await api_ctrl.create(api)
    return {"API_key": api_key}


@api_router.post("/add-partner")
async def add_partner(partner: AddPartner):
    api_controller = APIController()
    new_partner = await api_controller.add_partner(
        partner.user_id,
        partner.api_key,
        partner.permission)
    return {"new_partner": new_partner}


@api_router.post("/balance")
async def get_balance(
        API_KEY:Annotated[str | None, Header()],
        income_offset: int = 0, income_limit: int = 0,
        withdrawal_offset: int = 0, withdrawal_limit: int = 0
):
    api_ctrl = APIController()
    # transaction_history = await api_ctrl.transaction_history(API_KEY, income_offset, income_limit)
    # withdrawal_history = await api_ctrl.withdrawal_history(API_KEY, withdrawal_offset, withdrawal_limit)
    balance = await api_ctrl.get_balance(API_KEY)
    return {
        "balance": balance,
        # "withdrawal_history":withdrawal_history,
        # "transaction_history": transaction_history
        }


@api_router.post("/withdrawal")
async def withdrawal(
        USER_ID: Annotated[str | None, Header()],
        API_KEY: Annotated[str | None, Header()],
        withdrawal: WithdrawalSchema
):

    withdrawal_ctrl = WithdrawalController()
    await withdrawal_ctrl.transfer(
        user_id=USER_ID,
        api_key=API_KEY,
        to=withdrawal.to,
        amount=withdrawal.amount
    )
    return {
        "withdrawal": withdrawal.amount
    }
