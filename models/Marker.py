from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class Marker(Document):
    address: str
    category: list[str]
    lat: str
    lng: str
    comments: list[dict['userId': str, "comment": str, "date": str]]
    dumbBells: float  # 0-5

    class Settings:
        name = "markers"
