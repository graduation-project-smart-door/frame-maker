from sqlalchemy import insert

from database.models import UserModel
from domain.user import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def create(self, user: User) -> User:
        query = insert(UserModel).values(**user.dict(exclude={'id'}))

        user.id = await self.database.execute(query)
        return user
