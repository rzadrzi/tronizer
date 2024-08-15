import os
from typing import Annotated, Tuple
from datetime import datetime, timedelta

from fastapi import APIRouter, Header, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from controllers import PurchaseController
from web.schema.schema import PaymentSchema

templates_path = str(os.path.join(os.getcwd(), "app", "web", "templates"))

templates = Jinja2Templates(directory=templates_path)


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


@customer_router.post("/purchase-query")
async def purchase_query(api_key, payment: PaymentSchema):
    if payment.amount == 0 or payment.amount is None:
        raise HTTPException(status_code=400, detail="amount can not be 0")
    purchase_controller = PurchaseController()
    purchase, wallet = await purchase_controller.create(api_key=api_key, amount=payment.amount)
    purchase_page = await purchase_controller.create_page(purchase)
    return {"purchase": f"{purchase}", "wallet": f"{wallet}"}


@customer_router.get("/purchase/{purchase_token}", response_class=HTMLResponse)
async def purchase_query_get(request: Request, purchase_token: str):
    purchase_controller = PurchaseController()
    get_page = await purchase_controller.get_page(purchase_token)

    x = get_page.expiration_at - datetime.now().timestamp()
    if x > 0:
        timer = x
    else:
        timer = None
    return templates.TemplateResponse(
        request=request, name="qrcode.html", context={"timer": timer}
    )
