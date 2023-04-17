from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    label: str
    id: Optional[int] = None
