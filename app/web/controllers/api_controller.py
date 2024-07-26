from uuid import uuid4

import pymongo
import tldextract
from beanie import WriteRules
from fastapi import HTTPException
from controllers import UserController
from models import APIModel, PartnerModel
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
            partner = PartnerModel(user_id=user, permission=True)

            api = APIModel(
                api_key=api_key,
                owner=user,
                url=api.url,
                domain=domain,
                partner=[partner]
            )
            await api.insert(link_rule=WriteRules.WRITE)

        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=f"{e}")
        return api.api_key

    async def get_balance(self, api_key: str) -> float:
        api = await self.get_one(api_key)
        return api.balance

    async def update_balance(self, api_key: str, amount: float):
        api = await self.get_one(api_key)
        api.total_balance += amount
        await api.save()
        return api

    async def add_partner(self, api_key: str, user_id: str, permission: bool = False):
        user_ctrl = UserController()
        user = await user_ctrl.get_one(user_id=user_id)
        api = await self.get_one(api_key)
        partner = PartnerModel(user=user, permission=permission)
        api.partner.append(partner)
        await api.save()
        return api
