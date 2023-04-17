from sqlalchemy import insert, select

from database.models import UserModel
from domain.user import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def create(self, user: User) -> User:
        query = insert(UserModel).values(**user.dict(exclude={'id'}))

        user.id = await self.database.execute(query)
        return user

    async def all(self) -> list[User]:
        query = select(UserModel)

        return self.models_to_domains(await self.database.fetch_all(query))

    @classmethod
    def models_to_domains(cls, models: list[UserModel]) -> list[User]:
        return [cls.model_to_domain(model) for model in models]

    @staticmethod
    def model_to_domain(model: UserModel) -> User:
        return User(id=model.id, label=model.label)
