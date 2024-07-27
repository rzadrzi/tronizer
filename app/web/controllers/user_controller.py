from uuid import uuid4

from fastapi import HTTPException

from models import UserModel
from schema import UserSchema


class UserController:

    async def get_one(self, user_id: str):
        user = await UserModel.find_one(UserModel.user_id == user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User does not exists")
        return user

    async def create(self, user: UserSchema) -> str:
        try:
            user_id = uuid4().hex
            user_id = "TZ" + user_id[:12]
            user = UserModel(
                user_id=user_id,
                username=user.username,
                password=user.password,
                phone_number=user.phone_number,
                email=user.email
            )
            await user.insert()
            return user.user_id
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"User already exists {e}")

    async def get_balance(self, user_id: str) -> float:
        user = await self.get_one(user_id)
        return user.total_balance

    async def update_balance(self, user_id: str, amount: float):
        user = await self.get_one(user_id)
        user.total_balance += amount
        await user.save()
        return user
