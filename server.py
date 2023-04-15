import os

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from environs import Env

import requests

import frame_maker

app = FastAPI()

env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")
HOST = env.str("HOST")
PORT = env.str("PORT")


class VideoType(BaseModel):
    file_path: str


class UserData(BaseModel):
    video: VideoType
    first_name: str
    last_name: str


@app.post("/video")
async def create_video(user: UserData):
    file_path = user.video.file_path

    url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    response = requests.get(url)

    with open("video.mp4", "wb") as f:
        f.write(response.content)

    frame_maker.start_make_frames(
        "video.mp4",
        user_data={
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    )

    os.remove("video.mp4")

    return {"message": "success"}


if __name__ == "__main__":
    uvicorn.run("server:app", host=HOST, port=PORT, reload=True)
