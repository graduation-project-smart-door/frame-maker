import os
import uuid

import requests
from fastapi import APIRouter, Depends

from api.dependencies.database import get_repository
from api.dependencies.settings import get_settings
from core.settings import AppSettings
from domain.user import User
from repositories.user import UserRepository
from schemas.user import CreateUser
from utils import frame_maker

router = APIRouter()


@router.post('/video')
async def create_video(
    user: CreateUser,
    settings: AppSettings = Depends(get_settings),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
):
    # file_path = user.video.file_path
    #
    # url = f'https://api.telegram.org/file/bot{settings.token}/{file_path}'
    #
    # response = requests.get(url)
    #
    # with open("video.mp4", "wb") as file:
    #     file.write(response.content)
    #
    # frame_maker.start_make_frames(
    #     'video.mp4',
    #     user_data={
    #         'first_name': user.first_name,
    #         'last_name': user.last_name,
    #     },
    # )
    #
    # os.remove('video.mp4')

    label = f'{user.first_name}_{user.last_name}--{uuid.uuid4()}'

    await user_repository.create(User(label=label))
    return {'message': 'success'}
