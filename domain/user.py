from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    label: str
    id: Optional[int] = None
