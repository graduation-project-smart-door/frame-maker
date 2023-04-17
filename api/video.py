import os
import uuid

import requests
from fastapi import APIRouter, Depends
from starlette import status
from transliterate import translit

from api.dependencies.database import get_repository
from api.dependencies.settings import get_settings
from core.settings import AppSettings
from domain.user import User
from repositories.user import UserRepository
from schemas.user import CreateUser
from utils import frame_maker

router = APIRouter()


@router.post('/video', status_code=status.HTTP_201_CREATED)
async def create_video(
    user: CreateUser,
    settings: AppSettings = Depends(get_settings),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
):
    file_path = user.video.file_path

    url = f'https://api.telegram.org/file/bot{settings.token}/{file_path}'

    response = requests.get(url)

    uuid_value = uuid.uuid4()

    with open("video.mp4", "wb") as file:
        file.write(response.content)

    frame_maker.start_make_frames(
        'video.mp4',
        user_data={
            'first_name': user.first_name,
            'last_name': user.last_name,
        },
        uuid_value=uuid_value,
    )

    os.remove('video.mp4')

    label = f'{translit(user.first_name, language_code="ru", reversed=True)}_{translit(user.last_name, language_code="ru", reversed=True)}--{uuid_value}'

    await user_repository.create(User(label=label))
    return {'message': 'success'}
