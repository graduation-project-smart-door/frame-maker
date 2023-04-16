from fastapi import APIRouter

from api import video

router = APIRouter()

router.include_router(video.router, tags=['Users'], prefix='/api/')
