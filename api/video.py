import os

import requests
from fastapi import APIRouter

from schemas.user import CreateUser
from utils import frame_maker

router = APIRouter()


@router.post("/video")
async def create_video(user: CreateUser, token: str):
    file_path = user.video.file_path

    url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    response = requests.get(url)

    with open("video.mp4", "wb") as file:
        file.write(response.content)

    frame_maker.start_make_frames(
        "video.mp4",
        user_data={
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    )

    os.remove("video.mp4")

    return {"message": "success"}
