
from datetime import datetime, timedelta
from typing import Tuple, Type
from uuid import uuid4

from beanie import WriteRules
from fastapi import HTTPException

import config
from coins import TRON
from controllers import WalletController, APIController
from models import PurchaseModel


class PurchaseController:

    async def get_one(self, purchase_token):
        p = await PurchaseModel.find_one(PurchaseModel.purchase_token==purchase_token)
        if p is None:
            raise HTTPException(status_code=404, detail="Purchase was not created")
        return p

    async def create(self,  api_key: str,  amount: float) -> Type[tuple]:
        settings = config.Settings()
        api_controller = APIController()
        api = await api_controller.get_one(api_key=api_key)

        wallet_controller = WalletController()
        wallet = await wallet_controller.choice()

        t = TRON(settings.TRONGRID, wallet.public_key, wallet.private_key)
        old_balance = await t.usdt.balance()
        expiration_at = (datetime.now() + timedelta(minutes=30)).timestamp()

        purchase_token = uuid4().hex

        purchase = await PurchaseModel(
            purchase_token=purchase_token,
            api=api,
            wallet=wallet,
            amount=amount,
            balance=old_balance,
            is_open=True,
            expiration_at=expiration_at
        )
        await purchase.insert(link_rule=WriteRules.WRITE)

        return Tuple[purchase.purchase_token, wallet.public_key]

    async def get_all_openes_purchase(self):
        all = await PurchaseModel.find(PurchaseModel.is_open==True).to_list()
        if len(all) == 0:
            print("all Purchases was closed")
        return all
