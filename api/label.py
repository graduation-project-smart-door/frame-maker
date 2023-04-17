from fastapi import APIRouter, Depends

from api.dependencies.database import get_repository
from repositories.user import UserRepository

router = APIRouter()


@router.get('')
async def all_labels(
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> list[str]:
    return [item.label for item in await user_repository.all()]
