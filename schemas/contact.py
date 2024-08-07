from pydantic import BaseModel, EmailStr
from typing import Optional, Any

class UpdateContactModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    message: Optional[str]

    class Collection:
        name = "contact"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Felipe serrano antil",
                "email": "felpez@santil.com",
                "message": "felpez",
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
