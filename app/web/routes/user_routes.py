
from fastapi import APIRouter

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

#
# @user_router.post("/get-one")
# async def get_one(user_id: str):
#     user_controller = UserController()
#     user = await user_controller.get_one(user_id)
#     return {"user": user}
