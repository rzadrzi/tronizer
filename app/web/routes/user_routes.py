
from fastapi import APIRouter

# from web.controllers.user_controllers import UserController
# from web.schema.schema import UserSchema

from controllers import UserController
from schema import UserSchema


user_router = APIRouter(
    prefix="/user"
)


@user_router.post("/create")
async def create_user(user: UserSchema):
    uctlr = UserController()
    user_id = await uctlr.create(user)
    return {"USER_ID": user_id}
