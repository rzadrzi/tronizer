from beanie import WriteRules
from fastapi import HTTPException

import config
from coins import TRON
from controllers import APIController
from models import WithdrawalModel
from schema import WithdrawalStatus


class WithdrawalController:
    def __init__(self):
        self.settings = config.Settings()
        self.mom_wallet = TRON(
            self.settings.TRONGRID,
            self.settings.PUBLIC_KEY,
            self.settings.PRIVATE_KEY
        )

    async def transfer(self, user_id: str, api_key: str, to: str, amount: float):
        if to is None:
            raise HTTPException(status_code=400, detail="wallet can not be empty")

        if amount == 0 or amount is None:
            raise HTTPException(status_code=400, detail="amount can not be 0")

        api_controller = APIController()
        partner = api_controller.get_one_partner(user_id, api_key)
        api = await api_controller.get_one(api_key)

        if api.balance < amount:
            raise HTTPException(status_code=406, detail="Not Acceptable")

        withdrawal = WithdrawalModel(partner=partner, amount=amount, to=to)
        await withdrawal.insert(link_rule=WriteRules.WRITE)

        amount_after = self.calculator(amount=amount)
        try:
            trn = await self.mom_wallet.usdt.transaction(to=to, amount=int(amount_after))
            withdrawal.status = WithdrawalStatus.success
            api.balance = api.balance - amount
            await withdrawal.save(link_rule=WriteRules.WRITE)
            await api.save(link_rule=WriteRules.WRITE)
            return trn

        except Exception as e:
            print("Error: ", e)

    def calculator(self, amount):
        if amount < 10:
            raise HTTPException(status_code=405, detail="the amount must be more than 5 USDT")
        if amount < 100:
            return amount - 5
        elif 100 < amount < 500:
            return amount * 0.96
        elif 500 < amount < 1000:
            return amount * 0.97
        elif 1000 < amount < 10000:
            return amount * 0.98
        else:
            return amount * 0.99
