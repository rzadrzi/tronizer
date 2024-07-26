
from fastapi import APIRouter

from controllers import APIController
from schema import APISchema, AddPartner


api_router = APIRouter(
    prefix="/api"
)


@api_router.post("/create")
async def create_api(api: APISchema):
    api_ctrl = APIController()
    api_key = await api_ctrl.create(api)
    return {"API_key": api_key}


@api_router.post("add-partner")
async def add_partner(partner: AddPartner):
    api_controller = APIController()
    new_partner = await api_controller.add_partner(
        partner.user_id,
        partner.api_key,
        partner.permission)
    return {"new_partner": new_partner}

