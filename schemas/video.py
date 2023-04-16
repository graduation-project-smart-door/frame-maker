from pydantic import BaseModel


class VideoType(BaseModel):
    file_path: str
