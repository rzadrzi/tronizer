from uuid import uuid4

import pymongo
import tldextract
from beanie import WriteRules
from fastapi import HTTPException
from controllers import UserController
from models import APIModel, PartnerModel, PurchaseCloneModel, WithdrawalModel
from schema import APISchema


class APIController:

    async def get_one(self, api_key: str):
        api = await APIModel.find_one(APIModel.api_key == api_key)
        if api is None:
            raise HTTPException(status_code=404, detail="API does not exists")
        return api

    async def create(self, api: APISchema) -> str:
        user_ctrl = UserController()
        user = await user_ctrl.get_one(user_id=api.user_id)

        try:
            d = tldextract.extract(api.url)
            domain = d.domain + "." + d.suffix
            str_uuid = uuid4().hex
            api_key = "TZ" + str_uuid + "ER"

            api = APIModel(
                api_key=api_key,
                owner=user,
                url=api.url,
                domain=domain
            )
            await api.insert(link_rule=WriteRules.WRITE)

            partner = PartnerModel(user=user, api=api, permission=True)
            await partner.insert(link_rule=WriteRules.WRITE)

        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=f"{e}")
        return api.api_key

    async def add_partner(self, user_id: str, api_key: str, permission: bool = False):
        user_ctrl = UserController()
        user = await user_ctrl.get_one(user_id)
        api = await self.get_one(api_key)

        try:
            partner = PartnerModel(user=user, api=api, permission=permission)
            await partner.insert(link_rule=WriteRules.WRITE)
            return partner
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Partner does not added: {e}")

    async def get_one_partner(self, user_id: str, api_key: str):
        try:
            partner = await PartnerModel.find_one(
                PartnerModel.user.user_id==user_id,
                PartnerModel.api.api_key == api_key
            )
            return partner
        except Exception as e:
            raise HTTPException(status_code=404, detail="user id or api key is not true")

    async def get_balance(self, api_key: str) -> float:
        api = await self.get_one(api_key)
        return api.balance

    async def update_balance(self, api_key: str, amount: float):
        api = await self.get_one(api_key)
        api.total_balance += amount
        await api.save()
        return api

    async def transaction_history(self, api_key: str, offset: int, limit: int):
        c = await PurchaseCloneModel.find(PurchaseCloneModel.api_key==api_key)\
            .sort([(PurchaseCloneModel.create_at, pymongo.ASCENDING),])\
                .skip(offset)\
                    .limit(limit)\
                        .to_list()
        return c

    async def withdrawal_history(self, api_key: str, offset: int, limit: int):
        w = await WithdrawalModel.find(WithdrawalModel.api_key==api_key)\
            .sort([(WithdrawalModel.create_at, pymongo.ASCENDING),])\
                .skip(offset)\
                    .limit(limit)\
                        .to_list()
        return w



