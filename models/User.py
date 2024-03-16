from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    username: str  # Hashed
    password: str
    firstname: str
    lastname: str



    class Settings:
        name = "users"
