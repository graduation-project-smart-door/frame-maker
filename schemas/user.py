from pydantic import BaseModel

from schemas.video import VideoType


class CreateUser(BaseModel):
    video: VideoType
    first_name: str
    last_name: str
    person_id: str
