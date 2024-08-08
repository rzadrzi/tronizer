from typing import Annotated

from fastapi import APIRouter, Header, HTTPException
from fastapi.responses import JSONResponse

from controllers import PurchaseController
from web.schema.schema import PaymentSchema

customer_router = APIRouter(
    prefix="/customer"
)


@customer_router.post("/purchase")
async def purchase(API_KEY: Annotated[str | None, Header()], payment: PaymentSchema):
    if payment.amount == 0 or payment.amount is None:
        raise HTTPException(status_code=400, detail="amount can not be 0")
    purchase_controller = PurchaseController()
    purchase, wallet = await purchase_controller.create(api_key=API_KEY, amount=payment.amount)
    content = {"wallet": wallet}
    headers = {"PURCHASE_TOKEN": purchase}
    return JSONResponse(content=content, headers=headers)


@customer_router.post("/confirm")
async def confirm(PURCHASE_TOKEN: Annotated[str | None, Header()]):
    purchase_controller = PurchaseController()
    clone = await purchase_controller.get_clone(purchase_token=PURCHASE_TOKEN)
    return {"confirm": clone}
