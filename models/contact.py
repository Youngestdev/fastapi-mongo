from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class Contact(Document):
    name: str
    email: EmailStr
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Relete fuentes gordas",
                "email": "relente@fuentes.com",
                "message": "Consulta información",
            }
        }

    class Settings:
        name = "contact"
