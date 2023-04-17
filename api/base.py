from fastapi import APIRouter

from api import video, label

router = APIRouter()

router.include_router(video.router, tags=['Users'], prefix='/api/users')
router.include_router(label.router, tags=['Labels'], prefix='/api/labels')
